def nologin(view_func):
    """
    Decorator for views that marks them as allowed without authentication.
    """
    view_func.nologin = True
    return view_func