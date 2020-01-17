import pytest
from sqlalchemy import event

from database.database import db_session, engine


# pytest fixtures

@pytest.yield_fixture(scope='function')
def protect_db():  # used to have the 'db' fixture as a param
    """
    Creates a new database session for a test. Note you must use this fixture
    if your test connects to db.
    Here we not only support commit calls but also rollback calls in tests,
    :coolguy:.
    """
    connection = engine.connect()
    transaction = connection.begin()

    db_session.begin_nested()

    # session is actually a scoped_session
    # for the `after_transaction_end` event, we need a session instance to
    # listen for, hence the `session()` call
    @event.listens_for(db_session(), 'after_transaction_end')
    def restart_savepoint(sess, trans):
        if trans.nested and not trans._parent.nested:
            db_session.expire_all()
            db_session.begin_nested()

    yield db_session

    db_session.remove()
    transaction.rollback()
    connection.close()