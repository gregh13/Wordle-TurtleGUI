from turtle import Screen
from word_list import common_words_list, dictionary
from square import Square
from letters import Letters
from keyboard import Keyboard
import random


def make_guess():
    user_guess = screen.textinput("Make A Guess", "Write a valid 5 letter word").lower()
    if user_guess in dictionary:
        return user_guess
    else:
        screen.textinput("No Bueno", f"'{user_guess}' is not a valid 5 letter word. Please try again.")
        return make_guess()


def make_guess_final():
    user_guess = screen.textinput("FINAL GUESS", "One more guess, make it count!").lower()
    if user_guess in dictionary:
        return user_guess
    else:
        screen.textinput("No Bueno", f"'{user_guess}' is not a valid 5 letter word. Please try again.")
        return make_guess()


WIDTH = 420
HEIGHT = 750
STRETCH_FACTOR = 3

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgpic("keyboard_best.png")
guesses = 0
chosen_word = random.choice(common_words_list)

screen.tracer(0)
square = Square(STRETCH_FACTOR, HEIGHT, chosen_word)
letter = Letters(STRETCH_FACTOR, HEIGHT)
keyboard = Keyboard()


# For testing purposes:
# print(f"Chosen word = {chosen_word}")

game_is_on = True
while game_is_on:
    if guesses < 5:
        user_guess = make_guess()
        bad_letters = square.guess_feedback(user_guess)
        letter.write_guess(user_guess)
        keyboard.stamp_out(bad_letters)
        if user_guess == chosen_word:
            game_is_on = False
            screen.textinput("GAME OVER", f"You got it! Congrats :)\nThe word was indeed: {chosen_word}")
        if game_is_on:
            guesses += 1
    elif guesses == 5:
        user_guess = make_guess_final()
        bad_letters = square.guess_feedback_final(user_guess)
        letter.write_guess_final(user_guess)
        keyboard.stamp_out(bad_letters)
        if user_guess == chosen_word:
            game_is_on = False
            screen.textinput("GAME OVER", f"Phew, you got it just in time! Congrats :)\n\nThe word was indeed: {chosen_word}")
        if game_is_on:
            guesses += 1
    elif guesses == 6:
        game_is_on = False
        screen.textinput("GAME OVER", f"You ran out of guesses :(\nThe word was: {chosen_word}")
    screen.update()

screen.exitonclick()
