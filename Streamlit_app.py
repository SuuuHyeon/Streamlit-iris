{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOeJy2KVgnURQip185qqwYo",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SuuuHyeon/Streamlit-iris/blob/main/Streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.datasets import load_iris\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "import joblib\n",
        "\n",
        "X,y = load_iris(return_X_y=True)\n",
        "model = RandomForestClassifier()\n",
        "model.fit(X,y)\n",
        "joblib.dump(model,'model.pkl')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EB17xjq0H-Ng",
        "outputId": "475ad76b-aba3-46f2-e04c-31497f9501c7"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['model.pkl']"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "import numpy as np\n",
        "import joblib\n",
        "\n",
        "model = joblib.load(\"model.pkl\")\n",
        "\n",
        "st.title(\"꽃 분류(Iris Classifier)\")\n",
        "st.write(\"입력값을 기반으로 꽃의 종류를 예측합니다.\")\n",
        "\n",
        "sepal_length = st.slider(\"Sepal Length\", 0.0, 10.0, 5.0)\n",
        "sepal_width = st.slider(\"Sepal Width\", 0.0, 10.0, 5.0)\n",
        "petal_length = st.slider(\"Petal Length\", 0.0, 10.0, 5.0)\n",
        "petal_width = st.slider(\"Petal Width\", 0.0, 10.0, 5.0)\n",
        "\n",
        "input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])\n",
        "prediction = model.predict(input_data)\n",
        "\n",
        "predicted_class = prediction[0]\n",
        "\n",
        "class_names = [\"Setosa\", \"Versicolor\", \"Virginica\"]\n",
        "\n",
        "st.subheader(\"예측 결과\")\n",
        "st.write(f\"-> {class_names[predicted_class]}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5KZZNQEfHtR7",
        "outputId": "cf7718f8-8f83-4173-fe6d-6850f47e8952"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-06-04 08:53:06.420 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.422 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.426 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.427 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.430 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.431 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.431 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.434 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.435 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.436 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.437 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.438 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.439 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.442 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.444 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.444 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.446 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.447 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.449 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.449 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.451 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.454 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.475 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.477 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.480 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-06-04 08:53:06.483 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "viO61gZoHtG-"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}