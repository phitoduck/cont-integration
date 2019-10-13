import app

def test_error():

    try:
        app.error(True)
    except:
        assert True
    else:
        assert False