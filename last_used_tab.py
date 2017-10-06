import sublime_plugin
import sublime

view_stack = {

}


# Logging
# Uncomment "next(log1)" and "next(log2)" below to see log statements.
count = 0
def logger(func_name):
    global count
    from os.path import basename
    while True:
        print ('{} {}:\t'.format(func_name, count), {window: [[label, basename(x.view().file_name()) if x is not None and x.view().file_name() is not None else None] for (label, x) in dic.items()] for (window, dic) in view_stack.items()}, end='\n\n')
        count += 1
        yield

log1 = logger('Command')
log2 = logger('Listener')


def update():
    window_id = sublime.active_window().id()

    if window_id not in view_stack:
        view_stack[window_id] = {'last_view': None, 'current_view': None}

    if view_stack[window_id]['current_view'] == sublime.active_window().active_sheet():
        return

    view_stack[window_id]['last_view'] = view_stack[window_id]['current_view']
    view_stack[window_id]['current_view'] = sublime.active_window().active_sheet()


class LastUsedTabCommand(sublime_plugin.WindowCommand):
    def run(self):
        global view_stack

        window_id = sublime.active_window().id()

        # next(log1)
        sublime.active_window().focus_sheet(view_stack[window_id]['last_view'])
        update() # Necessary, if focus is on console while running the commmand for instance


class LastUsedTabListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        global view_stack

        update()

        # next(log2)
