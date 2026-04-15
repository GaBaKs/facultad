extends CharacterBody2D

@export var speed: float = 200.0

@export var joystick_path: NodePath

@onready var joystick = get_node(joystick_path)

func _physics_process(delta: float) -> void:
	# Obtiene la dirección desde el joystick
	var direction: Vector2 = joystick.output

	# Aplica movimiento
	velocity = direction * speed
	move_and_slide()
