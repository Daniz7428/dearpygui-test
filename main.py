import dearpygui.dearpygui as dpg
vp = dpg.create_viewport(title="caca", width=600, height=200)

with dpg.window(label="cacaculo"):
    dpg.add_text("hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="makro gei")
    dpg.add_slider_float(label="float", default_value=0.069, max_value=1)

dpg.setup_dearpygui(viewport=vp)
dpg.show_viewport(vp)

dpg.start_dearpygui()

