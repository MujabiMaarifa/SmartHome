/*
since we are changing the static facts(usually unchanged) we need to declare the predicate sensors and devices as dynamic
:- is a declarative 
*/
:- dynamic sensor/2 .
:- dynamic device/2 . %predicate_device_with_two_arguments

%facts
motion_detected.
time_is_night.
temperature(15).
smoke_detected.
gas_leak.
home_owner_not_home.
door_opened.
window_broken.

%sensor_facts_based_room_sensorType_value
sensor(living_room, temperature(20)).
sensor(living_room, motion_detected).
sensor(bedroom, temperature(29)).
sensor(bedroom, motion_detected).
sensor(kitchen, gas_leak).
sensor(apartment, smoke_detected).

%device(deviceName, status)
device(heater, off).
device(air_conditioner, off).
device(light, off).
device(gas_knob, off).
device(door_sensor, off).
device(fire_alarm, off).

%heaterRules
turn_on(heater, Room):-
	sensor(Room, temperature(T)),
	T < 20 .

%airConditioner
turn_on(air_conditioner, Room):-
	sensor(Room, temperature(T)),
	T > 25 .

%lights
turn_on(lights, Room):-
	sensor(Room, motion_detected),
	time_is_night.

%alarm
turn_on(fire_alarm, Room):-
	sensor(Room, smoke_detected),
	sensor(Room, temperature(T)),
	T>25 .

unlock_all_doors(door_sensor, Room):-
	turn_on(fire_alarm, Room).

%turn_off_gas_knob
turn_off(gas_knob, Room):-
	sensor(Room, gas_leak).

%helper_dynamic_updates
set_device_state(Device, NewState):-
	retract(device(Device, _)),
	assert(device(Device, NewState)).


