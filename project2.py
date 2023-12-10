import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.weight_label = ttk.Label(root, text="Weight (kg):")
        self.weight_entry = ttk.Entry(root)

        self.height_label = ttk.Label(root, text="Height (m):")
        self.height_entry = ttk.Entry(root)

        self.calculate_button = ttk.Button(root, text="Calculate BMI", command=self.calculate_bmi)

        self.result_label = ttk.Label(root, text="BMI Result:")
        self.result_value = ttk.Label(root, text="")

        self.plot_button = ttk.Button(root, text="Plot BMI History", command=self.plot_bmi_history)

        # Pack widgets
        self.weight_label.pack(pady=5)
        self.weight_entry.pack(pady=5)

        self.height_label.pack(pady=5)
        self.height_entry.pack(pady=5)

        self.calculate_button.pack(pady=10)

        self.result_label.pack(pady=5)
        self.result_value.pack(pady=5)

        self.plot_button.pack(pady=10)

        # Initialize data storage (for demonstration purposes)
        self.data = pd.DataFrame(columns=['Weight', 'Height', 'BMI'])

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            # Correct BMI calculation formula
            bmi = (weight / (height/100)**2 )
            self.result_value.config(text=f"BMI: {bmi:.2f}")

            # Save data to DataFrame
            new_data = pd.DataFrame({'Weight': [weight], 'Height': [height], 'BMI': [bmi]})
            self.data = pd.concat([self.data, new_data], ignore_index=True)

        except ValueError:
            self.result_value.config(text="Invalid input. Please enter numeric values.")

    def plot_bmi_history(self):
        if not self.data.empty:
            fig, ax = plt.subplots()
            ax.plot(self.data.index, self.data['BMI'], marker='o', linestyle='-', color='b')
            ax.set(xlabel='Entry', ylabel='BMI', title='BMI History')
            ax.grid()
            plt.xticks(rotation=45)

            canvas = FigureCanvasTkAgg(fig, master=self.root)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack()

        else:
            self.result_value.config(text="No data available for plotting.")


if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
