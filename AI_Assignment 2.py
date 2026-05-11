{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e0b9110f-d02e-49b6-85e7-b0e6a28b1527",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f3d5b899-ac8a-403c-9236-d00196df6670",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=======================================================\n",
      "        TASK 1: DATASET\n",
      "=======================================================\n",
      "Std   Math     Science    English    Computer   Result\n",
      "-------------------------------------------------------\n",
      "S1    85       90         78         92         Pass\n",
      "S2    45       50         40         55         Fail\n",
      "S3    70       65         80         75         Pass\n",
      "S4    30       35         28         40         Fail\n",
      "S5    95       88         91         97         Pass\n",
      "S6    60       72         65         58         Pass\n",
      "S7    48       42         55         38         Fail\n",
      "S8    82       79         85         88         Pass\n",
      "S9    55       60         50         62         Pass\n",
      "S10   20       25         30         22         Fail\n"
     ]
    }
   ],
   "source": [
    "print(\"=\" * 55)\n",
    "print(\"        Task 1: Dataset\")\n",
    "print(\"=\" * 55)\n",
    "data = np.array([\n",
    "    [85, 90, 78, 92, 1],   # Student 1\n",
    "    [45, 50, 40, 55, 0],   # Student 2\n",
    "    [70, 65, 80, 75, 1],   # Student 3\n",
    "    [30, 35, 28, 40, 0],   # Student 4\n",
    "    [95, 88, 91, 97, 1],   # Student 5\n",
    "    [60, 72, 65, 58, 1],   # Student 6\n",
    "    [48, 42, 55, 38, 0],   # Student 7\n",
    "    [82, 79, 85, 88, 1],   # Student 8\n",
    "    [55, 60, 50, 62, 1],   # Student 9\n",
    "    [20, 25, 30, 22, 0],   # Student 10\n",
    "])\n",
    " \n",
    "subjects = [\"Math\", \"Science\", \"English\", \"Computer\"]\n",
    "print(f\"{'Std':<5} {'Math':<8} {'Science':<10} {'English':<10} {'Computer':<10} {'Result'}\")\n",
    "print(\"-\" * 55)\n",
    "for i, row in enumerate(data):\n",
    "    result = \"Pass\" if row[4] == 1 else \"Fail\"\n",
    "    print(f\"S{i+1:<4} {row[0]:<8} {row[1]:<10} {row[2]:<10} {row[3]:<10} {result}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "136792ca-ca02-48a3-9aaa-7868d3276f91",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "========================================\n",
      "        TASK 2: DATA PROCESSING\n",
      "========================================\n",
      "\n",
      "--- Features (X) ---\n",
      "[[85 90 78 92]\n",
      " [45 50 40 55]\n",
      " [70 65 80 75]\n",
      " [30 35 28 40]\n",
      " [95 88 91 97]\n",
      " [60 72 65 58]\n",
      " [48 42 55 38]\n",
      " [82 79 85 88]\n",
      " [55 60 50 62]\n",
      " [20 25 30 22]]\n",
      "\n",
      "--- Labels (y) ---\n",
      "[1 0 1 0 1 1 0 1 1 0]\n",
      "\n",
      "--- Average Marks per Subject ---\n",
      "  Math      : 59.00\n",
      "  Science   : 60.60\n",
      "  English   : 60.20\n",
      "  Computer  : 62.70\n",
      "\n",
      "--- Highest Marks per Subject ---\n",
      "  Math      : 95\n",
      "  Science   : 90\n",
      "  English   : 91\n",
      "  Computer  : 97\n",
      "\n",
      "--- Lowest Marks per Subject ---\n",
      "  Math      : 20\n",
      "  Science   : 25\n",
      "  English   : 28\n",
      "  Computer  : 22\n",
      "\n",
      "--- Students with ANY mark above 80 ---\n",
      "  Student 1: Math=85, Science=90, Computer=92\n",
      "  Student 5: Math=95, Science=88, English=91, Computer=97\n",
      "  Student 8: Math=82, English=85, Computer=88\n",
      "\n",
      "--- Students with ANY mark below 50 ---\n",
      "  Student 2: Math=45, English=40\n",
      "  Student 4: Math=30, Science=35, English=28, Computer=40\n",
      "  Student 7: Math=48, Science=42, Computer=38\n",
      "  Student 10: Math=20, Science=25, English=30, Computer=22\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n\" + \"=\" * 40)\n",
    "print(\"        TASK 2: DATA PROCESSING\")\n",
    "print(\"=\" * 40)\n",
    "X = data[:, :4]   \n",
    "y = data[:, 4] \n",
    "print(\"\\n--- Features (X) ---\")\n",
    "print(X)\n",
    "print(\"\\n--- Labels (y) ---\")\n",
    "print(y)\n",
    " \n",
    "\n",
    "print(\"\\n--- Average Marks per Subject ---\")\n",
    "for i, subj in enumerate(subjects):\n",
    "    print(f\"  {subj:<10}: {X[:, i].mean():.2f}\")\n",
    " \n",
    "print(\"\\n--- Highest Marks per Subject ---\")\n",
    "for i, subj in enumerate(subjects):\n",
    "    print(f\"  {subj:<10}: {X[:, i].max()}\")\n",
    " \n",
    "print(\"\\n--- Lowest Marks per Subject ---\")\n",
    "for i, subj in enumerate(subjects):\n",
    "    print(f\"  {subj:<10}: {X[:, i].min()}\")\n",
    " \n",
    "print(\"\\n--- Students with ANY mark above 80 ---\")\n",
    "for i, row in enumerate(X):\n",
    "    above_80 = [(subjects[j], row[j]) for j in range(4) if row[j] > 80]\n",
    "    if above_80:\n",
    "        details = \", \".join(f\"{s}={m}\" for s, m in above_80)\n",
    "        print(f\"  Student {i+1}: {details}\")\n",
    " \n",
    "print(\"\\n--- Students with ANY mark below 50 ---\")\n",
    "for i, row in enumerate(X):\n",
    "    below_50 = [(subjects[j], row[j]) for j in range(4) if row[j] < 50]\n",
    "    if below_50:\n",
    "        details = \", \".join(f\"{s}={m}\" for s, m in below_50)\n",
    "        print(f\"  Student {i+1}: {details}\")\n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c8002f9-f1c6-47dd-b42a-fecd9906476c",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"\\n\" + \"=\" * 55)\n",
    "print(\"        TASK 3: NORMALIZED DATA\")\n",
    "print(\"=\" * 55)\n",
    "X_min = X.min(axis=0)   # Min per subject (column-wise)\n",
    "X_max = X.max(axis=0)   # Max per subject (column-wise)\n",
    " \n",
    "X_norm = (X - X_min) / (X_max - X_min)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
