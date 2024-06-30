from utilitarios.vpython_manager import VpythonManager
import vpython as vp

if __name__ == '__main__':
    # # Create a text object
    # text_obj = vp.text(text='dasdasdasd', align='center', color=vp.color.red, background=vp.color.white)
    # text_obj.pos = vp.vector(0, 0, 0)  # Positioning the first text object

    # # Create a second text object
    # text_obj2 = vp.text(text='dasdasdasd2', align='center', color=vp.color.red, background=vp.color.white)
    # text_obj2.pos = vp.vector(0, 2, 0)  # Positioning the second text object

    # # Set the scene properties
    # vp.scene.background = vp.color.white
    # vp.scene.center = vp.vector(0, 0, 0)  # Centering the scene to show both objects
    # vp.scene.autoscale = True
    # vp.scene.width = 700
    # print(os.get_terminal_size())
    sistema = VpythonManager()

    sistema.adicionar_titulo("Simulação de Cinemática e Dinâmica de uma Partícula")
    # Display text input prompt in the console
    user_input = input("Enter something: ")