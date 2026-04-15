extends Control

@export var max_radius: float = 80.0

# Vector de salida del joystick (valores entre -1 y 1)
var output: Vector2 = Vector2.ZERO

# Identificador del dedo que controla el joystick
var touch_id: int = -1

# Centro del joystick
var center: Vector2

# Referencia al knob (la palanca)
@onready var knob: Sprite2D = $Knob


func _ready() -> void:
	# Espera un frame para asegurar que el tamaño esté correctamente calculado
	await get_tree().process_frame
	
	# Calcula el centro del joystick
	center = size / 2
	
	# Coloca el knob en el centro
	knob.position = center - knob.size / 2


func _input(event: InputEvent) -> void:
	if event is InputEventScreenTouch:
		if event.pressed:
			# Si ningún dedo está controlando el joystick, se asigna este
			if touch_id == -1:
				touch_id = event.index
				_update_joystick(event.position)
		else:
			# Si se suelta el dedo que controlaba el joystick, se reinicia
			if event.index == touch_id:
				_reset_joystick()

	elif event is InputEventScreenDrag:
		# Si el dedo que se mueve es el que controla el joystick
		if event.index == touch_id:
			_update_joystick(event.position)


func _update_joystick(global_pos: Vector2) -> void:
	# Convierte la posición global de la pantalla a coordenadas locales del Control
	var local_pos: Vector2 = get_global_transform().affine_inverse() * global_pos
	
	# Calcula la dirección desde el centro
	var direction: Vector2 = local_pos - center
	
	# Limita el movimiento al radio máximo
	if direction.length() > max_radius:
		direction = direction.normalized() * max_radius
	
	# Mueve el knob
	knob.position = center + direction - knob.size / 2
	
	# Devuelve un vector normalizado entre -1 y 1
	output = direction / max_radius


func _reset_joystick() -> void:
	touch_id = -1
	output = Vector2.ZERO
	
	# Regresa el knob al centro
	knob.position = center - knob.size / 2
