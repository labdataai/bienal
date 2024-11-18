import recursos.c_usuario_controlador as cu
import recursos.c_ventana_perfil as vp

control_usuarios=cu.usuario_controlador()
control_usuarios.cargar_usuarios()

print(control_usuarios.usuarios)

ventana_principal=vp.ventana_perfil(control_usuarios)



