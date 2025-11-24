from pyswip import Prolog

prolog = Prolog()
prolog.consult("smart_home.pl")

def check_actions(room):
    print(f"\n***** Checking Actions for {room} *****")
    actions = list(prolog.query(f"turn_on(Device, {room})"))

    if not actions:
        print("No actions required.")

    else:
        for action in actions:
            device = action["Device"]
            print(f"* Should turn on {device}")

            list(prolog.query(f"set_device_state({device}, on)"))

def show_devices():
    print("@__ Device states __@")
    for row in prolog.query("device(Device, State)"):
        print(f"{row['Device']} : {row['State']}")

def update_sensor(room, sensor, value):
    print(f"^^ Updating System : {sensor} in {room} -> {value} ^^")
    list(prolog.query(f"retract(sensor({room}, _))"))
    list(prolog.query(f"assert(sensor({room}, {value}))"))

show_devices()
check_actions("bedroom")
check_actions("living_room")
check_actions("apartment")
check_actions("kitchen")
show_devices()




