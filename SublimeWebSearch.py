import sublime
import sublime_plugin
import webbrowser


class SearchAbstract(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = [self.view.substr(region) for region in self.view.sel()]
        if not self.search_url:
            settings = sublime.load_settings("SublimeWebSearch.sublime-settings")
            url = settings.get('custom_url')
            self.search_url = (url if url else 'http://stackoverflow.com/search?q=') + '%s'
        webbrowser.open(self.search_url % ''.join(selection))

    def is_visible(self):
        return True

    def is_enabled(self):
        return any((not region.empty()) for region in self.view.sel())


class GoogleSearchCommand(SearchAbstract):
    def __init__(self, *args, **kwargs):
        super(GoogleSearchCommand, self).__init__(*args, **kwargs)
        self.search_url = "https://www.google.com/search?q=%s"


class DuckduckgoSearchCommand(SearchAbstract):
    def __init__(self, *args, **kwargs):
        super(DuckduckgoSearchCommand, self).__init__(*args, **kwargs)
        self.search_url = "https://duckduckgo.com/?q=%s"


class CustomSearchCommand(SearchAbstract):
    def __init__(self, *args, **kwargs):
        super(CustomSearchCommand, self).__init__(*args, **kwargs)
        self.search_url = None
