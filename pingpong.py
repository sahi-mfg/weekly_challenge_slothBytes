""" 
A game of table tennis almost always sound like Ping! followed by Pong!

You know that Player 2 won if you hear Pong! as the last sound (since Player 2 didn't return the ball back)

Given an array of Ping!, create a function that inserts Pong! in between each element. Also:

- If win equals true, end the list with Pong!
- if win equals false, end the list with Ping!

>> pingPong(["Ping!"], True)
>> ["Ping!", "Pong!"]

>> pingPong(["Ping!", "Ping!"], False)
>> ["Ping!", "Pong!", "Ping!"]

>> pingPong(["Ping!", "Ping!", "Ping!"], True)
>> ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]

"""



def pin_pong(ping_array: list[str], win: bool = True) -> list[str]:
    pass