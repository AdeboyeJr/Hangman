from display import View

def test_view_init():
    view = View(None, None, None, "images/hm_0.png", "apple")
    assert view is not None
    assert view.img == "images/hm_0.png"
    assert view.word == "apple"


def test_view_render():
    pass

def test_view_show_text():
    pass

def test_view_get_lines():
    pass
    