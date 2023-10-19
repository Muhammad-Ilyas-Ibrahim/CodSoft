import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt


class RockPaperScissorsGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Rock Paper Scissors")
        self.setGeometry(80, 80, 400, 200)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()

        self.buttons_layout = QHBoxLayout()

        self.rock_button = QPushButton("Rock")
        self.rock_button.clicked.connect(lambda: self.play_round("Rock"))

        self.paper_button = QPushButton("Paper")
        self.paper_button.clicked.connect(lambda: self.play_round("Paper"))

        self.scissors_button = QPushButton("Scissors")
        self.scissors_button.clicked.connect(
            lambda: self.play_round("Scissors"))

        self.buttons_layout.addWidget(self.rock_button)
        self.buttons_layout.addWidget(self.paper_button)
        self.buttons_layout.addWidget(self.scissors_button)

        self.layout.addLayout(self.buttons_layout)

        self.score_layout = QVBoxLayout()
        self.game_score_label = QLabel("Game Score:")
        self.score_layout.addWidget(self.game_score_label)
        self.layout.addLayout(self.score_layout)

        self.user_score_label = QLabel("User: 0")
        self.computer_score_label = QLabel("Computer: 0")
        self.score_layout.addWidget(self.user_score_label)
        self.score_layout.addWidget(self.computer_score_label)

        self.reset_button = QPushButton("Reset Game")
        self.reset_button.clicked.connect(self.reset_game)
        self.layout.addWidget(self.reset_button)

        self.centralWidget.setLayout(self.layout)

        self.user_wins = 0
        self.computer_wins = 0
        self.game_number = 1

    def play_round(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "It's a Tie!"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors")
            or (player_choice == "Paper" and computer_choice == "Rock")
            or (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "Player Wins!"
            self.user_wins += 1
        else:
            result = "Computer Wins!"
            self.computer_wins += 1

        self.show_result_message(result, player_choice, computer_choice)
        self.update_scores()

    def show_result_message(self, result, player_choice, computer_choice):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(f"Game {self.game_number} - Round Result")
        msg_box.setText(f"{result}\n"
                        f"Player chose: {player_choice}\n"
                        f"Computer chose: {computer_choice}")
        msg_box.exec_()

    def update_scores(self):
        self.user_score_label.setText(f"User: {self.user_wins}")
        self.computer_score_label.setText(f"Computer: {self.computer_wins}")

    def reset_game(self):
        self.game_number += 1
        self.user_wins = 0
        self.computer_wins = 0
        self.user_score_label.setText("User: 0")
        self.computer_score_label.setText("Computer: 0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = RockPaperScissorsGame()
    game.show()
    sys.exit(app.exec_())
