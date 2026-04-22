{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jZOX8yFRhOf1",
        "outputId": "05b3f44d-65df-442b-ef90-77a549f30319"
      },
      "source": [
        "attempts = 5\n",
        "password_is_strong = False\n",
        "\n",
        "while attempts > 0:\n",
        "    password = input(f\"Enter your password: \")\n",
        "    length_check = len(password) >= 8\n",
        "    digit_check = any(char.isdigit() for char in password)\n",
        "    uppercase_check = any(char.isupper() for char in password)\n",
        "\n",
        "    conditions_met = sum([length_check, digit_check, uppercase_check])\n",
        "    feedback = \"\"\n",
        "    if conditions_met == 0:\n",
        "        feedback = \"Very Weak\"\n",
        "    elif conditions_met == 1:\n",
        "        feedback = \"Weak\"\n",
        "    elif conditions_met == 2:\n",
        "        feedback = \"Normal\"\n",
        "    else:\n",
        "        feedback = \"Strong\"\n",
        "\n",
        "    print(f\"Password strength: {feedback}\")\n",
        "\n",
        "    if feedback == \"Strong\":\n",
        "        print(f\"You created a strong password!\")\n",
        "        password_is_strong = True\n",
        "        break\n",
        "\n",
        "    attempts -= 1\n",
        "    if attempts > 0:\n",
        "        print(f\"Remaining attempts: {attempts}\")\n",
        "if not password_is_strong:\n",
        "    print(f\"Final Result: Password is not strong.\")"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your password: toni\n",
            "Password strength: Very Weak\n",
            "Remaining attempts: 4\n",
            "Enter your password: qtspin\n",
            "Password strength: Very Weak\n",
            "Remaining attempts: 3\n",
            "Enter your password: ailabb\n",
            "Password strength: Very Weak\n",
            "Remaining attempts: 2\n",
            "Enter your password: tonimoni13March\n",
            "Password strength: Strong\n",
            "You created a strong password!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "wQWjPFCHhw9O"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
