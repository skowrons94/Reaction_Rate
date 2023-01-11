from ipywidgets import interactive_output, widgets, HBox, VBox, Layout

def CreateWidgets( run ):
    style = {'description_width': 'initial'}

    temperature = widgets.FloatText(value=0.01, step=0.001,
                                    continuous_update=False,
                                    description='Temperature (GK):',
                                    style=style,
                                    disabled=False)
    
    scale = widgets.Select(options=['Linear',
                                    'Log'],
                           value='Linear',
                           description='Plot Scale:',
                           disabled=False)

    layout = Layout(border='2px solid grey',
                    width='1050px',
                    height='',
                    flex_flow='row',
                    display='flex',
                    justify_content = 'center')

    left_box = VBox([temperature])
    right_box = VBox([scale])

    ui = HBox([left_box, right_box], layout=layout)
    w = interactive_output(run,
                           { 
                               "T": temperature,
                               "scale": scale
                           })

    return ui, w
