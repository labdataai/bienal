import recursos.c_ventana_texto as vt
import recursos.c_usuario_controlador as cu

control_usuarios=cu.usuario_controlador()
control_usuarios.cargar_usuarios()
ventana=vt.ventana_texto(control_usuarios)
ventana.start()