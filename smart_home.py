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

    doors_windows = list(prolog.query(f"open_(Device, {room})"))
    if not doors_windows:
        print("No actions required for doors and windows")
    else:
        for door_window in doors_windows:
            device = door_window["Device"]
            print(f"* Opening {device}")

            list(prolog.query(f"set_device_state({device}, on)"))

    gas_knob_on = list(prolog.query(f"turn_off(Device, {room})"))
    if gas_knob_on:
        device = gas_knob_on[0]["Device"]
        print(f"* Closing {device}")
        list(prolog.query(f"set_device_state({device}, off)"))
    else:
        print("No gas leak detected. Always consider tightening the gas knob after use")

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




