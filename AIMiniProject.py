{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ca94fa7e-eddb-4caf-bcf3-654eb25b0abc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "31da898b-f263-47a3-9f5b-7bdd23c11961",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n",
      "     NumPy for AI — Student Performance Analysis          \n",
      "\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "  TASK 1: DATASET (12 Students)\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "  ID    Math     Science    English    Computer   Result\n",
      "  ───────────────────────────────────────────────────────\n",
      "  S1    78       85         80         90         ✔ Pass\n",
      "  S2    45       50         40         55         ✘ Fail\n",
      "  S3    92       88         95         97         ✔ Pass\n",
      "  S4    30       25         35         28         ✘ Fail\n",
      "  S5    65       70         60         75         ✔ Pass\n",
      "  S6    82       79         88         84         ✔ Pass\n",
      "  S7    48       55         42         50         ✘ Fail\n",
      "  S8    55       60         58         62         ✔ Pass\n",
      "  S9    20       30         25         22         ✘ Fail\n",
      "  S10   74       80         70         85         ✔ Pass\n",
      "  S11   88       91         85         93         ✔ Pass\n",
      "  S12   40       38         45         35         ✘ Fail\n"
     ]
    }
   ],
   "source": [
    "dataset = np.array([\n",
    "    [78, 85, 80, 90, 1],   # Student 1\n",
    "    [45, 50, 40, 55, 0],   # Student 2\n",
    "    [92, 88, 95, 97, 1],   # Student 3\n",
    "    [30, 25, 35, 28, 0],   # Student 4\n",
    "    [65, 70, 60, 75, 1],   # Student 5\n",
    "    [82, 79, 88, 84, 1],   # Student 6\n",
    "    [48, 55, 42, 50, 0],   # Student 7\n",
    "    [55, 60, 58, 62, 1],   # Student 8\n",
    "    [20, 30, 25, 22, 0],   # Student 9\n",
    "    [74, 80, 70, 85, 1],   # Student 10\n",
    "    [88, 91, 85, 93, 1],   # Student 11\n",
    "    [40, 38, 45, 35, 0],   # Student 12\n",
    "])\n",
    " \n",
    "SUBJECTS = [\"Math\", \"Science\", \"English\", \"Computer\"]\n",
    "n_students = len(dataset)\n",
    "print(\" \\n     NumPy for AI — Student Performance Analysis          \")\n",
    "print(\"\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(\"  TASK 1: DATASET (12 Students)\")\n",
    "print(\"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(f\"  {'ID':<5} {'Math':<8} {'Science':<10} {'English':<10} {'Computer':<10} {'Result'}\")\n",
    "print(\"  \" + \"─\" * 55)\n",
    "for i, row in enumerate(dataset):\n",
    "    label = \"✔ Pass\" if row[4] == 1 else \"✘ Fail\"\n",
    "    print(f\"  S{i+1:<4} {row[0]:<8} {row[1]:<10} {row[2]:<10} {row[3]:<10} {label}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ea549163-980d-4922-b54d-20e9d704f55c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "  TASK 2: FEATURES (X) AND LABELS (y)\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "\n",
      "  X (Marks Matrix) — shape: (12, 4)\n",
      "  [[78. 85. 80. 90.]\n",
      " [45. 50. 40. 55.]\n",
      " [92. 88. 95. 97.]\n",
      " [30. 25. 35. 28.]\n",
      " [65. 70. 60. 75.]\n",
      " [82. 79. 88. 84.]\n",
      " [48. 55. 42. 50.]\n",
      " [55. 60. 58. 62.]\n",
      " [20. 30. 25. 22.]\n",
      " [74. 80. 70. 85.]\n",
      " [88. 91. 85. 93.]\n",
      " [40. 38. 45. 35.]]\n",
      "\n",
      "  y (Labels) — shape: (12,)\n",
      "  [1 0 1 0 1 1 0 1 0 1 1 0]\n"
     ]
    }
   ],
   "source": [
    "X = dataset[:, :4].astype(float)   # Features: marks\n",
    "y = dataset[:, 4].astype(int)      # Labels: pass/fail\n",
    " \n",
    "print(\"\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(\"  TASK 2: FEATURES (X) AND LABELS (y)\")\n",
    "print(\"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(f\"\\n  X (Marks Matrix) — shape: {X.shape}\")\n",
    "print(f\"  {X}\")\n",
    "print(f\"\\n  y (Labels) — shape: {y.shape}\")\n",
    "print(f\"  {y}\")\n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4d67e378-d8a5-46da-8db3-38e6f6fb4d8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "  TASK 3: STATISTICS PER SUBJECT\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "\n",
      "  Subject      Average      Maximum      Minimum\n",
      "  ─────────────────────────────────────────────\n",
      "  Math         59.75        92           20\n",
      "  Science      62.58        91           25\n",
      "  English      60.25        95           25\n",
      "  Computer     64.67        97           22\n",
      "\n",
      "  Overall Average (all subjects): 61.81\n",
      "  Overall Maximum: 97\n",
      "  Overall Minimum: 20\n"
     ]
    }
   ],
   "source": [
    "\n",
    "avg_marks = np.mean(X, axis=0)\n",
    "max_marks = np.max(X, axis=0)\n",
    "min_marks = np.min(X, axis=0)\n",
    " \n",
    "print(\"\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(\"  TASK 3: STATISTICS PER SUBJECT\")\n",
    "print(\"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(f\"\\n  {'Subject':<12} {'Average':<12} {'Maximum':<12} {'Minimum'}\")\n",
    "print(\"  \" + \"─\" * 45)\n",
    "for i, subj in enumerate(SUBJECTS):\n",
    "    print(f\"  {subj:<12} {avg_marks[i]:<12.2f} {max_marks[i]:<12.0f} {min_marks[i]:.0f}\")\n",
    " \n",
    "print(f\"\\n  Overall Average (all subjects): {np.mean(X):.2f}\")\n",
    "print(f\"  Overall Maximum: {np.max(X):.0f}\")\n",
    "print(f\"  Overall Minimum: {np.min(X):.0f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "055dd33b-cb9a-4d69-bf3f-6bc058d29083",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "  TASK 4: PASS / FAIL COUNT\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "\n",
      "  Total Students : 12\n",
      "  ✔ Passed       : 7  (58.3%)\n",
      "  ✘ Failed       : 5  (41.7%)\n"
     ]
    }
   ],
   "source": [
    "passed = np.sum(y == 1)\n",
    "failed = np.sum(y == 0)\n",
    " \n",
    "print(\"\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(\"  TASK 4: PASS / FAIL COUNT\")\n",
    "print(\"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(f\"\\n  Total Students : {n_students}\")\n",
    "print(f\"  ✔ Passed       : {passed}  ({passed/n_students*100:.1f}%)\")\n",
    "print(f\"  ✘ Failed       : {failed}  ({failed/n_students*100:.1f}%)\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fc169906-ca44-480b-ba3d-3b0b69e9fe80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "  TASK 5: SCORE FILTERS\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "\n",
      "  ► Students with at least one mark ABOVE 80:\n",
      "  ─────────────────────────────────────────────\n",
      "    S1: Science=85,  Computer=90\n",
      "    S3: Math=92,  Science=88,  English=95,  Computer=97\n",
      "    S6: Math=82,  English=88,  Computer=84\n",
      "    S10: Computer=85\n",
      "    S11: Math=88,  Science=91,  English=85,  Computer=93\n",
      "\n",
      "  ► Students with at least one mark BELOW 50:\n",
      "  ─────────────────────────────────────────────\n",
      "    S2: Math=45,  English=40\n",
      "    S4: Math=30,  Science=25,  English=35,  Computer=28\n",
      "    S7: Math=48,  English=42\n",
      "    S9: Math=20,  Science=30,  English=25,  Computer=22\n",
      "    S12: Math=40,  Science=38,  English=45,  Computer=35\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(\"\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(\"  TASK 5: SCORE FILTERS\")\n",
    "print(\"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    " \n",
    "print(\"\\n  ► Students with at least one mark ABOVE 80:\")\n",
    "print(\"  \" + \"─\" * 45)\n",
    "found = False\n",
    "for i, row in enumerate(X):\n",
    "    high_subjects = [(SUBJECTS[j], int(row[j])) for j in range(4) if row[j] > 80]\n",
    "    if high_subjects:\n",
    "        details = \",  \".join(f\"{s}={m}\" for s, m in high_subjects)\n",
    "        print(f\"    S{i+1}: {details}\")\n",
    "        found = True\n",
    "if not found:\n",
    "    print(\"    None found.\")\n",
    " \n",
    "print(\"\\n  ► Students with at least one mark BELOW 50:\")\n",
    "print(\"  \" + \"─\" * 45)\n",
    "found = False\n",
    "for i, row in enumerate(X):\n",
    "    low_subjects = [(SUBJECTS[j], int(row[j])) for j in range(4) if row[j] < 50]\n",
    "    if low_subjects:\n",
    "        details = \",  \".join(f\"{s}={m}\" for s, m in low_subjects)\n",
    "        print(f\"    S{i+1}: {details}\")\n",
    "        found = True\n",
    "if not found:\n",
    "    print(\"    None found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b59ce0ac-36d1-46c1-8cf5-fa54c81c1d2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "  TASK 6: NORMALIZED DATA  [formula: (x - min) / (max - min)]\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "\n",
      "  Min per subject : [20. 25. 25. 22.]\n",
      "  Max per subject : [92. 91. 95. 97.]\n",
      "\n",
      "  ID     Math       Science      English      Computer\n",
      "  ──────────────────────────────────────────────────\n",
      "  S1     0.8056     0.9091       0.7857       0.9067\n",
      "  S2     0.3472     0.3788       0.2143       0.4400\n",
      "  S3     1.0000     0.9545       1.0000       1.0000\n",
      "  S4     0.1389     0.0000       0.1429       0.0800\n",
      "  S5     0.6250     0.6818       0.5000       0.7067\n",
      "  S6     0.8611     0.8182       0.9000       0.8267\n",
      "  S7     0.3889     0.4545       0.2429       0.3733\n",
      "  S8     0.4861     0.5303       0.4714       0.5333\n",
      "  S9     0.0000     0.0758       0.0000       0.0000\n",
      "  S10    0.7500     0.8333       0.6429       0.8400\n",
      "  S11    0.9444     1.0000       0.8571       0.9467\n",
      "  S12    0.2778     0.1970       0.2857       0.1733\n",
      "\n",
      "  Note: 0.0 = lowest scorer | 1.0 = highest scorer (per subject)\n"
     ]
    }
   ],
   "source": [
    "X_min = X.min(axis=0)\n",
    "X_max = X.max(axis=0)\n",
    "X_norm = (X - X_min) / (X_max - X_min)\n",
    " \n",
    "print(\"\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(\"  TASK 6: NORMALIZED DATA  [formula: (x - min) / (max - min)]\")\n",
    "print(\"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(f\"\\n  Min per subject : {X_min}\")\n",
    "print(f\"  Max per subject : {X_max}\")\n",
    "print(f\"\\n  {'ID':<6} {'Math':<10} {'Science':<12} {'English':<12} {'Computer'}\")\n",
    "print(\"  \" + \"─\" * 50)\n",
    "for i, row in enumerate(X_norm):\n",
    "    print(f\"  S{i+1:<5} {row[0]:<10.4f} {row[1]:<12.4f} {row[2]:<12.4f} {row[3]:.4f}\")\n",
    "print(\"\\n  Note: 0.0 = lowest scorer | 1.0 = highest scorer (per subject)\")\n",
    " \n",
    " "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "481e4371-4972-4206-9480-75e8db165eac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "  TASK 7: PREDICTION  [Rule: avg marks >= 60 → Pass]\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "\n",
      "  ID     Avg Marks    Actual       Predicted    Match?\n",
      "  ───────────────────────────────────────────────────────\n",
      "  S1     83.25        Pass         Pass         ✔\n",
      "  S2     47.50        Fail         Fail         ✔\n",
      "  S3     93.00        Pass         Pass         ✔\n",
      "  S4     29.50        Fail         Fail         ✔\n",
      "  S5     67.50        Pass         Pass         ✔\n",
      "  S6     83.25        Pass         Pass         ✔\n",
      "  S7     48.75        Fail         Fail         ✔\n",
      "  S8     58.75        Pass         Fail         ✘ WRONG\n",
      "  S9     24.25        Fail         Fail         ✔\n",
      "  S10    77.25        Pass         Pass         ✔\n",
      "  S11    89.25        Pass         Pass         ✔\n",
      "  S12    39.50        Fail         Fail         ✔\n"
     ]
    }
   ],
   "source": [
    "avg_per_student = np.mean(X, axis=1)           # Average mark per student\n",
    "THRESHOLD = 60.0                                # Passing threshold\n",
    "y_pred = (avg_per_student >= THRESHOLD).astype(int)\n",
    " \n",
    "print(\"\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(\"  TASK 7: PREDICTION  [Rule: avg marks >= 60 → Pass]\")\n",
    "print(\"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(f\"\\n  {'ID':<6} {'Avg Marks':<12} {'Actual':<12} {'Predicted':<12} {'Match?'}\")\n",
    "print(\"  \" + \"─\" * 55)\n",
    "for i in range(n_students):\n",
    "    actual    = \"Pass\" if y[i] == 1 else \"Fail\"\n",
    "    predicted = \"Pass\" if y_pred[i] == 1 else \"Fail\"\n",
    "    match     = \"✔\" if y[i] == y_pred[i] else \"✘ WRONG\"\n",
    "    print(f\"  S{i+1:<5} {avg_per_student[i]:<12.2f} {actual:<12} {predicted:<12} {match}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "46ac2605-59b2-4f79-b9e7-af7e08004138",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "  TASK 8: ACCURACY & EVALUATION\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "\n",
      "  Total Students      : 12\n",
      "  Correct Predictions : 11\n",
      "  Wrong Predictions   : 1\n",
      "\n",
      "    ACCURACY = 11/12 × 100 = 91.67%\n",
      "\n",
      "  Confusion Matrix:\n",
      "  ┌─────────────────────┬──────────┬──────────┐\n",
      "  │                     │ Pred Pass│ Pred Fail│\n",
      "  ├─────────────────────┼──────────┼──────────┤\n",
      "  │ Actual Pass         │  TP=6    │  FN=1    │\n",
      "  │ Actual Fail         │  FP=0    │  TN=5    │\n",
      "  └─────────────────────┴──────────┴──────────┘\n",
      "\n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "                     PROJECT COMPLETE                           \n",
      "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n",
      "\n"
     ]
    }
   ],
   "source": [
    "\n",
    "correct     = np.sum(y == y_pred)\n",
    "accuracy    = (correct / n_students) * 100\n",
    " \n",
    "# Confusion matrix values\n",
    "TP = np.sum((y == 1) & (y_pred == 1))   # Predicted Pass, Actually Pass\n",
    "TN = np.sum((y == 0) & (y_pred == 0))   # Predicted Fail, Actually Fail\n",
    "FP = np.sum((y == 0) & (y_pred == 1))   # Predicted Pass, Actually Fail\n",
    "FN = np.sum((y == 1) & (y_pred == 0))   # Predicted Fail, Actually Pass\n",
    " \n",
    "print(\"\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(\"  TASK 8: ACCURACY & EVALUATION\")\n",
    "print(\"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(f\"\\n  Total Students      : {n_students}\")\n",
    "print(f\"  Correct Predictions : {correct}\")\n",
    "print(f\"  Wrong Predictions   : {n_students - correct}\")\n",
    "print(f\"\\n    ACCURACY = {correct}/{n_students} × 100 = {accuracy:.2f}%\")\n",
    " \n",
    "print(f\"\\n  Confusion Matrix:\")\n",
    "print(f\"  ┌─────────────────────┬──────────┬──────────┐\")\n",
    "print(f\"  │                     │ Pred Pass│ Pred Fail│\")\n",
    "print(f\"  ├─────────────────────┼──────────┼──────────┤\")\n",
    "print(f\"  │ Actual Pass         │  TP={TP:<4} │  FN={FN:<4} │\")\n",
    "print(f\"  │ Actual Fail         │  FP={FP:<4} │  TN={TN:<4} │\")\n",
    "print(f\"  └─────────────────────┴──────────┴──────────┘\")\n",
    " \n",
    "print(\"\\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\")\n",
    "print(\"                     PROJECT COMPLETE                           \")\n",
    "print(\"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\\n\")"
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
