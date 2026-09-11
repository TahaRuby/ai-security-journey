import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)
from PyQt6.QtCore import Qt


class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI Calculator")
        self.setFixedSize(400, 300)

        self.init_ui()

    def init_ui(self):
        # Title
        title = QLabel("BMI Calculator")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 15px;
        """)

        # Weight
        weight_label = QLabel("Weight (kg):")
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText(" 70")

        # Height
        height_label = QLabel("Height (cm):")
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText(" 175")

        # Calculate button
        calculate_button = QPushButton("Calculate BMI")
        calculate_button.clicked.connect(self.calculate_bmi)

        # Result
        self.result_label = QLabel("BMI: -")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            margin-top: 15px;
        """)

        # Layout
        layout = QVBoxLayout()

        layout.addWidget(title)

        layout.addWidget(weight_label)
        layout.addWidget(self.weight_input)

        layout.addWidget(height_label)
        layout.addWidget(self.height_input)

        layout.addSpacing(10)
        layout.addWidget(calculate_button)

        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_input.text())
            height_cm = float(self.height_input.text())

            if weight <= 0 or height_cm <= 0:
                raise ValueError

            height_m = height_cm / 100
            bmi = weight / (height_m ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            self.result_label.setText(
                f"BMI: {bmi:.2f}\n{category}"
            )

        except ValueError:
            QMessageBox.warning(
                self,
                "Invalid Input",
                "Enter a valid value :/"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BMICalculator()
    window.show()

    sys.exit(app.exec())
