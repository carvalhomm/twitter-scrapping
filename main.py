import user_interface as interface

gui = interface.UserInterface()
gui.generate_layout()
gui.draw_window()
gui.wait_for_user_interactions()
