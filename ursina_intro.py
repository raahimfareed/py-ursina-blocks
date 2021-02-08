from ursina import * # pylint: disable=unused-wildcard-import


class TestCube(Entity):
    def __init__(self):
        super().__init__(
            model="cube",
            color=color.white,
            texture="white_cube",
            rotation=Vec3(45, 45, 45),
            position=(-5, 5)
        )

class TestButton(Button):
    def __init__(self):
        super().__init__(
            parent= scene,
            model="cube",
            texture="brick",
            color=color.blue,
            highlight_color=color.red,
            pressed_color=color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                print("Button Pressed")


def update():
    if held_keys['a']:
        test_square.x -= 4 * time.dt

    if held_keys['d']:
        test_square.x += 4 * time.dt

    if held_keys['w']:
        test_square.y += 4 * time.dt

    if held_keys['s']:
        test_square.y -= 4 * time.dt


app = Ursina()

test_square = Entity(model="quad", color=color.red, scale=(1, 4), position=(5, 1))

sans_texture = load_texture("assets/Sans.png")
sans = Entity(model="quad", texture=sans_texture)

test_cube = TestCube()

test_button = TestButton()

app.run()
