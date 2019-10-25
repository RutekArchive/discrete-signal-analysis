import ipywidgets as widgets


class MainView:
    def __init__(self):
        self.input_signal_ploter = lambda signal_file, signal_key, one_plot: None
        self.output_signal_ploter = lambda signal_file, signal_key, transformation_name, one_plot: None

        self.signal_file_menu = widgets.Dropdown(
            value=None,
            description='Signals:',
        )

        self.signal_key_menu = widgets.Dropdown(
            value=None,
            description='Keys:',
        )

        self.transformation_menu = widgets.Dropdown(
            value=None,
            description='Transformations:',
        )

        self.one_plot_checkbox = widgets.Checkbox(
            value=True,
            description="One Plot",
            disabled=False,
        )

        self._plot_box = widgets.VBox()
        self.one_plot_checkbox.observe(self.on_one_plot_checkbox_change, "value", "change")

        self.input_signal_plot = widgets.interactive_output(lambda **kwargs: self.input_signal_ploter(**kwargs), {
            'signal_file': self.signal_file_menu,
            'signal_key': self.signal_key_menu,
            'one_plot': self.one_plot_checkbox,
        })

        self.signal_output_plot = widgets.interactive_output(lambda **kwargs: self.output_signal_ploter(**kwargs), {
            'signal_file': self.signal_file_menu,
            'signal_key': self.signal_key_menu,
            'transformation_name': self.transformation_menu,
            'one_plot': self.one_plot_checkbox,
        })

        self.on_one_plot_checkbox_change(dict(new=self.one_plot_checkbox.value))

        self.top_level = widgets.VBox([
            self.signal_file_menu,
            self.signal_key_menu,
            self.transformation_menu,
            self.one_plot_checkbox,
            self._plot_box,
        ])

    def on_one_plot_checkbox_change(self, kwargs):
        if kwargs['new']:
            self._plot_box.children = tuple([self.signal_output_plot])
        else:
            self._plot_box.children = tuple([self.signal_output_plot, self.input_signal_plot])
