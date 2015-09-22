import sublime_plugin
import sublime

view_stack = {

}


class LastUsedTabCommand(sublime_plugin.WindowCommand):
    def run(self):
        global view_stack

        window_id = sublime.active_window().id()
        sublime.active_window().focus_view(view_stack[window_id]['last_view'])


class LastUsedTabListener(sublime_plugin.EventListener):
    def on_activated(self, view):
        global view_stack
        window_id = sublime.active_window().id()

        if window_id not in view_stack:
            view_stack[window_id] = {'last_view': None, 'current_view': None}

        view_stack[window_id]['last_view'] = view_stack[window_id]['current_view']
        view_stack[window_id]['current_view'] = view
