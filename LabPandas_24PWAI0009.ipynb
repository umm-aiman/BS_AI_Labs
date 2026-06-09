{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3457d9cb-3170-4dc4-b82c-cf46e42e9988",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ All 3 dataset files created successfully!\n",
      "   customers.csv | purchases.csv | membership.xlsx\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# ── customers.csv ──\n",
    "customers_data = pd.DataFrame({\n",
    "    'CustomerID': list(range(101, 121)),\n",
    "    'Name': ['Ali','Sara','Ahmed','Fatima','Usman','Zara','Hassan','Ayesha','Bilal','Hina',\n",
    "             'Kamran','Sana','Tariq','Nida','Asad','Rabia','Imran','Maria','Faisal','Amna'],\n",
    "    'Age': [25, np.nan, 17, 35, 80, 28, 42, np.nan, 55, 31,\n",
    "            22, 45, np.nan, 60, 29, 38, 75, 26, 33, np.nan],\n",
    "    'Gender': ['M','F','M','F','M','f','M','F','m','F',\n",
    "               'M','F','M','F','M','F','M','F','M','F'],\n",
    "    'City':   ['Lahore','Karachi','lahore','ISLAMABAD','Karachi','Peshawar','lahore','Karachi',\n",
    "               'LAHORE','Islamabad','Peshawar','karachi','Lahore','islamabad','Karachi',\n",
    "               'Lahore','Peshawar','KARACHI','Islamabad','Lahore'],\n",
    "    'Income': [50000,70000,np.nan,90000,45000,-5000,120000,65000,np.nan,80000,\n",
    "               35000,55000,75000,np.nan,95000,40000,30000,85000,60000,np.nan]\n",
    "})\n",
    "# Add a duplicate row\n",
    "customers_data = pd.concat([customers_data, customers_data.iloc[[0]]], ignore_index=True)\n",
    "customers_data.to_csv('customers.csv', index=False)\n",
    "\n",
    "# ── purchases.csv ──\n",
    "purchases_data = pd.DataFrame({\n",
    "    'PurchaseID':  ['P001','P002','P003','P004','P005','P006','P007','P008','P009','P010','P002'],\n",
    "    'CustomerID':  [101,102,101,103,104,105,101,106,102,107,102],\n",
    "    'Product':     ['Laptop','Phone','Mouse','Laptop','Tablet','Phone','Keyboard','Monitor','Phone','Laptop','Phone'],\n",
    "    'Quantity':    [1,2,0,1,3,-1,2,1,1,2,2],\n",
    "    'Amount':      [90000,45000,np.nan,95000,60000,30000,8000,55000,np.nan,92000,45000]\n",
    "})\n",
    "purchases_data.to_csv('purchases.csv', index=False)\n",
    "\n",
    "# ── membership.xlsx ──\n",
    "membership_data = pd.DataFrame({\n",
    "    'CustomerID':     [101,102,103,105,106,108],\n",
    "    'MembershipType': ['Gold','silver','PLATINUM','Gold',None,'Silver'],\n",
    "    'JoinDate':       ['2024-01-05','2024-03-12','2023-11-20','2024-06-01','2024-02-15','2023-09-10']\n",
    "})\n",
    "membership_data.to_excel('membership.xlsx', index=False)\n",
    "\n",
    "print(\"✅ All 3 dataset files created successfully!\")\n",
    "print(\"   customers.csv | purchases.csv | membership.xlsx\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "72989566-f4e1-4385-b26e-d610f54127a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Files loaded successfully!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "customers  = pd.read_csv('customers.csv')\n",
    "purchases  = pd.read_csv('purchases.csv')\n",
    "membership = pd.read_excel('membership.xlsx', engine='openpyxl')\n",
    "\n",
    "print(\"Files loaded successfully!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ef0da47b-0182-4ca2-a46f-fdfaeaa42aa2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== CUSTOMERS (first 10) ===\n",
      "   CustomerID    Name   Age Gender       City    Income\n",
      "0         101     Ali  25.0      M     Lahore   50000.0\n",
      "1         102    Sara   NaN      F    Karachi   70000.0\n",
      "2         103   Ahmed  17.0      M     lahore       NaN\n",
      "3         104  Fatima  35.0      F  ISLAMABAD   90000.0\n",
      "4         105   Usman  80.0      M    Karachi   45000.0\n",
      "5         106    Zara  28.0      f   Peshawar   -5000.0\n",
      "6         107  Hassan  42.0      M     lahore  120000.0\n",
      "7         108  Ayesha   NaN      F    Karachi   65000.0\n",
      "8         109   Bilal  55.0      m     LAHORE       NaN\n",
      "9         110    Hina  31.0      F  Islamabad   80000.0\n",
      "\n",
      "=== PURCHASES (first 10) ===\n",
      "  PurchaseID  CustomerID   Product  Quantity   Amount\n",
      "0       P001         101    Laptop         1  90000.0\n",
      "1       P002         102     Phone         2  45000.0\n",
      "2       P003         101     Mouse         0      NaN\n",
      "3       P004         103    Laptop         1  95000.0\n",
      "4       P005         104    Tablet         3  60000.0\n",
      "5       P006         105     Phone        -1  30000.0\n",
      "6       P007         101  Keyboard         2   8000.0\n",
      "7       P008         106   Monitor         1  55000.0\n",
      "8       P009         102     Phone         1      NaN\n",
      "9       P010         107    Laptop         2  92000.0\n",
      "\n",
      "=== MEMBERSHIP (first 10) ===\n",
      "   CustomerID MembershipType    JoinDate\n",
      "0         101           Gold  2024-01-05\n",
      "1         102         silver  2024-03-12\n",
      "2         103       PLATINUM  2023-11-20\n",
      "3         105           Gold  2024-06-01\n",
      "4         106            NaN  2024-02-15\n",
      "5         108         Silver  2023-09-10\n"
     ]
    }
   ],
   "source": [
    "# First 10 rows\n",
    "print(\"=== CUSTOMERS (first 10) ===\")\n",
    "print(customers.head(10))\n",
    "print(\"\\n=== PURCHASES (first 10) ===\")\n",
    "print(purchases.head(10))\n",
    "print(\"\\n=== MEMBERSHIP (first 10) ===\")\n",
    "print(membership.head(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "de78a8d5-f535-4f49-b3cb-162149be7bc1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== CUSTOMERS (last 10) ===\n",
      "    CustomerID    Name   Age Gender       City   Income\n",
      "11         112    Sana  45.0      F    karachi  55000.0\n",
      "12         113   Tariq   NaN      M     Lahore  75000.0\n",
      "13         114    Nida  60.0      F  islamabad      NaN\n",
      "14         115    Asad  29.0      M    Karachi  95000.0\n",
      "15         116   Rabia  38.0      F     Lahore  40000.0\n",
      "16         117   Imran  75.0      M   Peshawar  30000.0\n",
      "17         118   Maria  26.0      F    KARACHI  85000.0\n",
      "18         119  Faisal  33.0      M  Islamabad  60000.0\n",
      "19         120    Amna   NaN      F     Lahore      NaN\n",
      "20         101     Ali  25.0      M     Lahore  50000.0\n",
      "\n",
      "=== PURCHASES (last 10) ===\n",
      "   PurchaseID  CustomerID   Product  Quantity   Amount\n",
      "1        P002         102     Phone         2  45000.0\n",
      "2        P003         101     Mouse         0      NaN\n",
      "3        P004         103    Laptop         1  95000.0\n",
      "4        P005         104    Tablet         3  60000.0\n",
      "5        P006         105     Phone        -1  30000.0\n",
      "6        P007         101  Keyboard         2   8000.0\n",
      "7        P008         106   Monitor         1  55000.0\n",
      "8        P009         102     Phone         1      NaN\n",
      "9        P010         107    Laptop         2  92000.0\n",
      "10       P002         102     Phone         2  45000.0\n"
     ]
    }
   ],
   "source": [
    "# Last 10 rows\n",
    "print(\"=== CUSTOMERS (last 10) ===\")\n",
    "print(customers.tail(10))\n",
    "print(\"\\n=== PURCHASES (last 10) ===\")\n",
    "print(purchases.tail(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e48fa335-890d-424a-816a-35cd982a3fd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "========================================\n",
      "  Customers\n",
      "  Shape      : (21, 6)\n",
      "  Columns    : ['CustomerID', 'Name', 'Age', 'Gender', 'City', 'Income']\n",
      "  Data Types :\n",
      "CustomerID      int64\n",
      "Name           object\n",
      "Age           float64\n",
      "Gender         object\n",
      "City           object\n",
      "Income        float64\n",
      "dtype: object\n",
      "\n",
      "========================================\n",
      "  Purchases\n",
      "  Shape      : (11, 5)\n",
      "  Columns    : ['PurchaseID', 'CustomerID', 'Product', 'Quantity', 'Amount']\n",
      "  Data Types :\n",
      "PurchaseID     object\n",
      "CustomerID      int64\n",
      "Product        object\n",
      "Quantity        int64\n",
      "Amount        float64\n",
      "dtype: object\n",
      "\n",
      "========================================\n",
      "  Membership\n",
      "  Shape      : (6, 3)\n",
      "  Columns    : ['CustomerID', 'MembershipType', 'JoinDate']\n",
      "  Data Types :\n",
      "CustomerID         int64\n",
      "MembershipType    object\n",
      "JoinDate          object\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "# Shape, columns, dtypes\n",
    "for name, df in [('Customers', customers), ('Purchases', purchases), ('Membership', membership)]:\n",
    "    print(f\"\\n{'='*40}\")\n",
    "    print(f\"  {name}\")\n",
    "    print(f\"  Shape      : {df.shape}\")\n",
    "    print(f\"  Columns    : {df.columns.tolist()}\")\n",
    "    print(f\"  Data Types :\\n{df.dtypes}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "80a8d5f0-0979-48e3-bcc5-21848b696214",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== CUSTOMERS SUMMARY ===\n",
      "       CustomerID        Age         Income\n",
      "count   21.000000  17.000000      17.000000\n",
      "mean   110.047619  39.176471   61176.470588\n",
      "std      6.127611  18.354956   29236.610812\n",
      "min    101.000000  17.000000   -5000.000000\n",
      "25%    105.000000  26.000000   45000.000000\n",
      "50%    110.000000  33.000000   60000.000000\n",
      "75%    115.000000  45.000000   80000.000000\n",
      "max    120.000000  80.000000  120000.000000\n",
      "\n",
      "=== PURCHASES SUMMARY ===\n",
      "       CustomerID   Quantity        Amount\n",
      "count   11.000000  11.000000      9.000000\n",
      "mean   103.090909   1.272727  57777.777778\n",
      "std      2.119177   1.103713  29965.721157\n",
      "min    101.000000  -1.000000   8000.000000\n",
      "25%    101.500000   1.000000  45000.000000\n",
      "50%    102.000000   1.000000  55000.000000\n",
      "75%    104.500000   2.000000  90000.000000\n",
      "max    107.000000   3.000000  95000.000000\n"
     ]
    }
   ],
   "source": [
    "# Summary statistics\n",
    "print(\"=== CUSTOMERS SUMMARY ===\")\n",
    "print(customers.describe())\n",
    "print(\"\\n=== PURCHASES SUMMARY ===\")\n",
    "print(purchases.describe())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "19c39f23-5777-4e65-82cb-6196dde53384",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Missing values BEFORE cleaning:\n",
      "\n",
      "Customers:\n",
      "CustomerID    0\n",
      "Name          0\n",
      "Age           4\n",
      "Gender        0\n",
      "City          0\n",
      "Income        4\n",
      "dtype: int64\n",
      "\n",
      "Purchases:\n",
      "PurchaseID    0\n",
      "CustomerID    0\n",
      "Product       0\n",
      "Quantity      0\n",
      "Amount        2\n",
      "dtype: int64\n",
      "\n",
      "Membership:\n",
      "CustomerID        0\n",
      "MembershipType    1\n",
      "JoinDate          0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# ── Missing Values BEFORE cleaning ──\n",
    "print(\"Missing values BEFORE cleaning:\")\n",
    "print(\"\\nCustomers:\")\n",
    "print(customers.isnull().sum())\n",
    "print(\"\\nPurchases:\")\n",
    "print(purchases.isnull().sum())\n",
    "print(\"\\nMembership:\")\n",
    "print(membership.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "37adeaad-47db-46a5-85a8-f86fafa67f9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Missing values filled.\n",
      "\n",
      "Missing values AFTER cleaning:\n",
      "Customers: 0\n",
      "Purchases: 0\n"
     ]
    }
   ],
   "source": [
    "# ── Fill Missing Values ──\n",
    "customers['Age']    = customers['Age'].fillna(customers['Age'].median())\n",
    "customers['Income'] = customers['Income'].fillna(customers['Income'].mean())\n",
    "customers['City']   = customers['City'].fillna('Unknown')\n",
    "purchases['Amount'] = purchases['Amount'].fillna(purchases['Amount'].median())\n",
    "\n",
    "print(\"✅ Missing values filled.\")\n",
    "print(\"\\nMissing values AFTER cleaning:\")\n",
    "print(\"Customers:\", customers.isnull().sum().sum())\n",
    "print(\"Purchases:\", purchases.isnull().sum().sum())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "f4443ec1-7390-4ca9-a068-37a9a9765b1f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Duplicates removed from customers : 1\n",
      "Duplicates removed from purchases : 1\n"
     ]
    }
   ],
   "source": [
    "# ── Duplicate Removal ──\n",
    "before_c = len(customers)\n",
    "before_p = len(purchases)\n",
    "\n",
    "customers = customers.drop_duplicates()\n",
    "purchases = purchases.drop_duplicates()\n",
    "\n",
    "print(f\"Duplicates removed from customers : {before_c - len(customers)}\")\n",
    "print(f\"Duplicates removed from purchases : {before_p - len(purchases)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "9398acbb-bc74-4409-8c34-0b0c2291059d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Standardization done.\n",
      "\n",
      "Unique Cities  : ['Lahore' 'Karachi' 'Islamabad' 'Peshawar']\n",
      "Unique Genders  : ['M' 'F']\n",
      "Unique Memberships: ['Gold' 'Silver' 'Platinum' nan]\n"
     ]
    }
   ],
   "source": [
    "# ── Data Standardization ──\n",
    "customers['City']   = customers['City'].str.strip().str.title()\n",
    "customers['Gender'] = customers['Gender'].str.strip().str.upper()\n",
    "membership['MembershipType'] = membership['MembershipType'].str.strip().str.title()\n",
    "\n",
    "print(\"✅ Standardization done.\")\n",
    "print(\"\\nUnique Cities  :\", customers['City'].unique())\n",
    "print(\"Unique Genders  :\", customers['Gender'].unique())\n",
    "print(\"Unique Memberships:\", membership['MembershipType'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "2872f7e1-676a-4d97-bfbb-d806179f61e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid ages (< 18 or > 70):\n",
      "    CustomerID   Name   Age\n",
      "2          103  Ahmed  17.0\n",
      "4          105  Usman  80.0\n",
      "16         117  Imran  75.0\n",
      "\n",
      "Negative Income:\n",
      "   CustomerID  Name  Income\n",
      "5         106  Zara -5000.0\n",
      "\n",
      "Invalid Quantity (<= 0):\n",
      "  PurchaseID  CustomerID  Quantity\n",
      "2       P003         101         0\n",
      "5       P006         105        -1\n",
      "\n",
      "✅ Outliers handled.\n",
      "Customers shape after cleaning: (19, 6)\n",
      "Purchases shape after cleaning: (8, 5)\n"
     ]
    }
   ],
   "source": [
    "# ── Outlier Detection & Handling ──\n",
    "print(\"Invalid ages (< 18 or > 70):\")\n",
    "print(customers[(customers['Age'] < 18) | (customers['Age'] > 70)][['CustomerID','Name','Age']])\n",
    "\n",
    "print(\"\\nNegative Income:\")\n",
    "print(customers[customers['Income'] < 0][['CustomerID','Name','Income']])\n",
    "\n",
    "print(\"\\nInvalid Quantity (<= 0):\")\n",
    "print(purchases[purchases['Quantity'] <= 0][['PurchaseID','CustomerID','Quantity']])\n",
    "\n",
    "# Fix outliers\n",
    "median_age = customers['Age'].median()\n",
    "customers.loc[(customers['Age'] < 18) | (customers['Age'] > 70), 'Age'] = median_age\n",
    "customers = customers[customers['Income'] >= 0].reset_index(drop=True)\n",
    "purchases = purchases[purchases['Quantity'] > 0].reset_index(drop=True)\n",
    "\n",
    "print(\"\\n✅ Outliers handled.\")\n",
    "print(f\"Customers shape after cleaning: {customers.shape}\")\n",
    "print(f\"Purchases shape after cleaning: {purchases.shape}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3795a7ef-6d33-4730-83e6-64bc391734e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== CLEANING REPORT ===\n",
      "              Check               Status\n",
      "        Missing Age   Filled with median\n",
      "     Missing Income     Filled with mean\n",
      "       Missing City  Filled with Unknown\n",
      "     Missing Amount   Filled with median\n",
      "Duplicate Customers              Removed\n",
      "Duplicate Purchases              Removed\n",
      "        Invalid Age Replaced with median\n",
      "    Negative Income          Row removed\n",
      "   Invalid Quantity          Row removed\n"
     ]
    }
   ],
   "source": [
    "# ── Cleaning Report ──\n",
    "report = pd.DataFrame({\n",
    "    'Check': ['Missing Age', 'Missing Income', 'Missing City', 'Missing Amount',\n",
    "              'Duplicate Customers', 'Duplicate Purchases',\n",
    "              'Invalid Age', 'Negative Income', 'Invalid Quantity'],\n",
    "    'Status': ['Filled with median', 'Filled with mean', 'Filled with Unknown',\n",
    "               'Filled with median', 'Removed', 'Removed',\n",
    "               'Replaced with median', 'Row removed', 'Row removed']\n",
    "})\n",
    "print(\"=== CLEANING REPORT ===\")\n",
    "print(report.to_string(index=False))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "fabd9807-c439-4c75-aba2-2b6800ccffb0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. Customers earning > 80,000: 4\n",
      "    CustomerID    Name    Income\n",
      "3          104  Fatima   90000.0\n",
      "5          107  Hassan  120000.0\n",
      "13         115    Asad   95000.0\n",
      "16         118   Maria   85000.0\n"
     ]
    }
   ],
   "source": [
    "# ── Filtering Tasks ──\n",
    "\n",
    "# 1. Customers earning above 80,000\n",
    "high_income = customers[customers['Income'] > 80000]\n",
    "print(f\"1. Customers earning > 80,000: {len(high_income)}\")\n",
    "print(high_income[['CustomerID','Name','Income']])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "594afda6-0861-4e47-80e5-e4ba311e46e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2. Female customers from Lahore: 2\n",
      "    CustomerID   Name Gender    City\n",
      "14         116  Rabia      F  Lahore\n",
      "18         120   Amna      F  Lahore\n"
     ]
    }
   ],
   "source": [
    "# 2. Female customers from Lahore\n",
    "female_lahore = customers[(customers['Gender'] == 'F') & (customers['City'] == 'Lahore')]\n",
    "print(f\"2. Female customers from Lahore: {len(female_lahore)}\")\n",
    "print(female_lahore[['CustomerID','Name','Gender','City']])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "5b81aac3-8551-4a2d-8e87-5ec67b241d3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3. Customers aged 25-40: 14\n",
      "    CustomerID    Name   Age\n",
      "0          101     Ali  25.0\n",
      "1          102    Sara  33.0\n",
      "2          103   Ahmed  33.0\n",
      "3          104  Fatima  35.0\n",
      "4          105   Usman  33.0\n",
      "6          108  Ayesha  33.0\n",
      "8          110    Hina  31.0\n",
      "11         113   Tariq  33.0\n",
      "13         115    Asad  29.0\n",
      "14         116   Rabia  38.0\n",
      "15         117   Imran  33.0\n",
      "16         118   Maria  26.0\n",
      "17         119  Faisal  33.0\n",
      "18         120    Amna  33.0\n"
     ]
    }
   ],
   "source": [
    "# 3. Customers aged between 25 and 40\n",
    "age_range = customers[(customers['Age'] >= 25) & (customers['Age'] <= 40)]\n",
    "print(f\"3. Customers aged 25-40: {len(age_range)}\")\n",
    "print(age_range[['CustomerID','Name','Age']])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "76e39b6e-abed-49d8-b5f5-404f5d8e3e47",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4. Purchases above 50,000: 6\n",
      "  PurchaseID  CustomerID  Product  Quantity   Amount\n",
      "0       P001         101   Laptop         1  90000.0\n",
      "2       P004         103   Laptop         1  95000.0\n",
      "3       P005         104   Tablet         3  60000.0\n",
      "5       P008         106  Monitor         1  55000.0\n",
      "6       P009         102    Phone         1  55000.0\n",
      "7       P010         107   Laptop         2  92000.0\n"
     ]
    }
   ],
   "source": [
    "# 4. Purchases above 50,000\n",
    "big_purchases = purchases[purchases['Amount'] > 50000]\n",
    "print(f\"4. Purchases above 50,000: {len(big_purchases)}\")\n",
    "print(big_purchases)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e56f81a7-5fb5-4345-8449-651b3d60a0e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5. Customers with more than 3 purchases: 0\n",
      "Empty DataFrame\n",
      "Columns: [CustomerID, Name]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "# 5. Customers with more than 3 purchases\n",
    "freq = purchases.groupby('CustomerID').size()\n",
    "top_buyers_ids = freq[freq > 3].index\n",
    "top_buyers = customers[customers['CustomerID'].isin(top_buyers_ids)]\n",
    "print(f\"5. Customers with more than 3 purchases: {len(top_buyers)}\")\n",
    "print(top_buyers[['CustomerID','Name']])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "578febf4-b445-4e55-9e91-260b9464fdf2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. Average Income by City:\n",
      "City\n",
      "Islamabad    72794.12\n",
      "Karachi      69166.67\n",
      "Lahore       66932.77\n",
      "Peshawar     32500.00\n",
      "Name: Income, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# ── Groupby Tasks ──\n",
    "\n",
    "# 1. Average income by city\n",
    "print(\"1. Average Income by City:\")\n",
    "print(customers.groupby('City')['Income'].mean().round(2))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "6fb134bc-8324-4546-afca-78d479377149",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2. Number of Customers per City:\n",
      "City\n",
      "Islamabad    4\n",
      "Karachi      6\n",
      "Lahore       7\n",
      "Peshawar     2\n",
      "Name: CustomerID, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# 2. Total sales by city (need merged — preview with customers only)\n",
    "print(\"2. Number of Customers per City:\")\n",
    "print(customers.groupby('City')['CustomerID'].count())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "084ed8b2-05e7-49fa-b79d-03e2372cea1d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3. Total Purchases by Gender:\n",
      "Gender\n",
      "F    160000.0\n",
      "M    285000.0\n",
      "Name: Amount, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# 3. Total purchases by gender\n",
    "print(\"3. Total Purchases by Gender:\")\n",
    "temp = customers.merge(purchases, on='CustomerID', how='left')\n",
    "print(temp.groupby('Gender')['Amount'].sum())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f9d11382-0b5c-430f-adfd-2bd23910c379",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4. Avg Purchase Amount by Membership Type:\n",
      "MembershipType\n",
      "Gold        49000.0\n",
      "Platinum    95000.0\n",
      "Silver      50000.0\n",
      "Name: Amount, dtype: float64\n",
      "\n",
      "5. Customer Count per City:\n",
      "City\n",
      "Lahore       7\n",
      "Karachi      6\n",
      "Islamabad    4\n",
      "Peshawar     2\n",
      "Name: count, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# 4. Average purchase amount by membership type (preview)\n",
    "temp2 = customers.merge(purchases, on='CustomerID', how='left')\n",
    "temp2 = temp2.merge(membership, on='CustomerID', how='left')\n",
    "print(\"4. Avg Purchase Amount by Membership Type:\")\n",
    "print(temp2.groupby('MembershipType')['Amount'].mean().round(2))\n",
    "\n",
    "# 5. Customer count per city\n",
    "print(\"\\n5. Customer Count per City:\")\n",
    "print(customers['City'].value_counts())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "820df827-01c4-4444-b1e2-326810e5315d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape after Merge 1 (customers + purchases): (21, 10)\n",
      "   CustomerID   Name   Age Gender     City        Income PurchaseID   Product  \\\n",
      "0         101    Ali  25.0      M   Lahore  50000.000000       P001    Laptop   \n",
      "1         101    Ali  25.0      M   Lahore  50000.000000       P007  Keyboard   \n",
      "2         102   Sara  33.0      F  Karachi  70000.000000       P002     Phone   \n",
      "3         102   Sara  33.0      F  Karachi  70000.000000       P009     Phone   \n",
      "4         103  Ahmed  33.0      M   Lahore  61176.470588       P004    Laptop   \n",
      "\n",
      "   Quantity   Amount  \n",
      "0       1.0  90000.0  \n",
      "1       2.0   8000.0  \n",
      "2       2.0  45000.0  \n",
      "3       1.0  55000.0  \n",
      "4       1.0  95000.0  \n"
     ]
    }
   ],
   "source": [
    "# ── Merge 1: customers + purchases ──\n",
    "merged = pd.merge(customers, purchases, on='CustomerID', how='left')\n",
    "print(f\"Shape after Merge 1 (customers + purchases): {merged.shape}\")\n",
    "print(merged.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "eadf3ff1-298d-45bd-a064-095d6dcef97c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape after Merge 2 (+ membership): (21, 12)\n",
      "   CustomerID   Name   Age Gender     City        Income PurchaseID   Product  \\\n",
      "0         101    Ali  25.0      M   Lahore  50000.000000       P001    Laptop   \n",
      "1         101    Ali  25.0      M   Lahore  50000.000000       P007  Keyboard   \n",
      "2         102   Sara  33.0      F  Karachi  70000.000000       P002     Phone   \n",
      "3         102   Sara  33.0      F  Karachi  70000.000000       P009     Phone   \n",
      "4         103  Ahmed  33.0      M   Lahore  61176.470588       P004    Laptop   \n",
      "\n",
      "   Quantity   Amount MembershipType    JoinDate  \n",
      "0       1.0  90000.0           Gold  2024-01-05  \n",
      "1       2.0   8000.0           Gold  2024-01-05  \n",
      "2       2.0  45000.0         Silver  2024-03-12  \n",
      "3       1.0  55000.0         Silver  2024-03-12  \n",
      "4       1.0  95000.0       Platinum  2023-11-20  \n"
     ]
    }
   ],
   "source": [
    "# ── Merge 2: merged + membership ──\n",
    "merged = pd.merge(merged, membership, on='CustomerID', how='left')\n",
    "print(f\"Shape after Merge 2 (+ membership): {merged.shape}\")\n",
    "print(merged.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b4a8a6e0-0881-4ed2-8434-2fd806c7d023",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Null values after merging:\n",
      "CustomerID         0\n",
      "Name               0\n",
      "Age                0\n",
      "Gender             0\n",
      "City               0\n",
      "Income             0\n",
      "PurchaseID        14\n",
      "Product           14\n",
      "Quantity          14\n",
      "Amount            14\n",
      "MembershipType    14\n",
      "JoinDate          14\n",
      "dtype: int64\n",
      "\n",
      "Matched records (have purchases)    : 7\n",
      "Unmatched (no purchase)              : 14\n",
      "Customers with no membership         : 14\n"
     ]
    }
   ],
   "source": [
    "# ── Post-merge analysis ──\n",
    "print(\"Null values after merging:\")\n",
    "print(merged.isnull().sum())\n",
    "\n",
    "no_purchase = merged[merged['PurchaseID'].isnull()]\n",
    "no_member   = merged[merged['MembershipType'].isnull()]\n",
    "matched     = merged[merged['PurchaseID'].notna()]\n",
    "\n",
    "print(f\"\\nMatched records (have purchases)    : {len(matched)}\")\n",
    "print(f\"Unmatched (no purchase)              : {len(no_purchase)}\")\n",
    "print(f\"Customers with no membership         : {len(no_member)}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1e5b05c5-19d2-4ac2-961e-100824e6bf14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== FINAL MERGED DATAFRAME ===\n",
      "    CustomerID    Name   Age Gender       City         Income PurchaseID   Product  Quantity   Amount MembershipType    JoinDate\n",
      "0          101     Ali  25.0      M     Lahore   50000.000000       P001    Laptop       1.0  90000.0           Gold  2024-01-05\n",
      "1          101     Ali  25.0      M     Lahore   50000.000000       P007  Keyboard       2.0   8000.0           Gold  2024-01-05\n",
      "2          102    Sara  33.0      F    Karachi   70000.000000       P002     Phone       2.0  45000.0         Silver  2024-03-12\n",
      "3          102    Sara  33.0      F    Karachi   70000.000000       P009     Phone       1.0  55000.0         Silver  2024-03-12\n",
      "4          103   Ahmed  33.0      M     Lahore   61176.470588       P004    Laptop       1.0  95000.0       Platinum  2023-11-20\n",
      "5          104  Fatima  35.0      F  Islamabad   90000.000000       P005    Tablet       3.0  60000.0            NaN         NaN\n",
      "6          105   Usman  33.0      M    Karachi   45000.000000        NaN       NaN       NaN      NaN           Gold  2024-06-01\n",
      "7          107  Hassan  42.0      M     Lahore  120000.000000       P010    Laptop       2.0  92000.0            NaN         NaN\n",
      "8          108  Ayesha  33.0      F    Karachi   65000.000000        NaN       NaN       NaN      NaN         Silver  2023-09-10\n",
      "9          109   Bilal  55.0      M     Lahore   61176.470588        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "10         110    Hina  31.0      F  Islamabad   80000.000000        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "11         111  Kamran  22.0      M   Peshawar   35000.000000        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "12         112    Sana  45.0      F    Karachi   55000.000000        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "13         113   Tariq  33.0      M     Lahore   75000.000000        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "14         114    Nida  60.0      F  Islamabad   61176.470588        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "15         115    Asad  29.0      M    Karachi   95000.000000        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "16         116   Rabia  38.0      F     Lahore   40000.000000        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "17         117   Imran  33.0      M   Peshawar   30000.000000        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "18         118   Maria  26.0      F    Karachi   85000.000000        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "19         119  Faisal  33.0      M  Islamabad   60000.000000        NaN       NaN       NaN      NaN            NaN         NaN\n",
      "20         120    Amna  33.0      F     Lahore   61176.470588        NaN       NaN       NaN      NaN            NaN         NaN\n"
     ]
    }
   ],
   "source": [
    "# Final merged DataFrame preview\n",
    "print(\"=== FINAL MERGED DATAFRAME ===\")\n",
    "print(merged.to_string())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ae4b2727-f988-407e-9506-b02b97129b4a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feature 1 — AgeGroup:\n",
      "    CustomerID   Age AgeGroup\n",
      "0          101  25.0    Young\n",
      "2          102  33.0    Adult\n",
      "4          103  33.0    Adult\n",
      "5          104  35.0    Adult\n",
      "6          105  33.0    Adult\n",
      "7          107  42.0    Adult\n",
      "8          108  33.0    Adult\n",
      "9          109  55.0   Senior\n",
      "10         110  31.0    Adult\n",
      "11         111  22.0    Young\n"
     ]
    }
   ],
   "source": [
    "# ── Feature 1: Age Group ──\n",
    "def age_group(age):\n",
    "    if age <= 30:   return 'Young'\n",
    "    elif age <= 50: return 'Adult'\n",
    "    else:           return 'Senior'\n",
    "\n",
    "merged['AgeGroup'] = merged['Age'].apply(age_group)\n",
    "print(\"Feature 1 — AgeGroup:\")\n",
    "print(merged[['CustomerID','Age','AgeGroup']].drop_duplicates().head(10))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "21a3a3fe-f4e5-443c-84a6-d95379472d24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feature 2 — IncomeCategory:\n",
      "    CustomerID         Income IncomeCategory\n",
      "0          101   50000.000000         Medium\n",
      "2          102   70000.000000         Medium\n",
      "4          103   61176.470588         Medium\n",
      "5          104   90000.000000           High\n",
      "6          105   45000.000000         Medium\n",
      "7          107  120000.000000           High\n",
      "8          108   65000.000000         Medium\n",
      "9          109   61176.470588         Medium\n",
      "10         110   80000.000000         Medium\n",
      "11         111   35000.000000            Low\n"
     ]
    }
   ],
   "source": [
    "# ── Feature 2: Income Category ──\n",
    "def income_cat(inc):\n",
    "    if inc < 40000:   return 'Low'\n",
    "    elif inc <= 80000: return 'Medium'\n",
    "    else:              return 'High'\n",
    "\n",
    "merged['IncomeCategory'] = merged['Income'].apply(income_cat)\n",
    "print(\"Feature 2 — IncomeCategory:\")\n",
    "print(merged[['CustomerID','Income','IncomeCategory']].drop_duplicates().head(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "ff6a2d2a-210f-49d4-a3e2-9bf3401fefb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feature 3 — SpendingScore (Amount x Quantity):\n",
      "   CustomerID   Amount  Quantity  SpendingScore\n",
      "0         101  90000.0       1.0        90000.0\n",
      "1         101   8000.0       2.0        16000.0\n",
      "2         102  45000.0       2.0        90000.0\n",
      "3         102  55000.0       1.0        55000.0\n",
      "4         103  95000.0       1.0        95000.0\n",
      "5         104  60000.0       3.0       180000.0\n",
      "6         105      NaN       NaN            0.0\n",
      "7         107  92000.0       2.0       184000.0\n",
      "8         108      NaN       NaN            0.0\n",
      "9         109      NaN       NaN            0.0\n"
     ]
    }
   ],
   "source": [
    "# ── Feature 3: Spending Score ──\n",
    "merged['SpendingScore'] = merged['Amount'].fillna(0) * merged['Quantity'].fillna(0)\n",
    "print(\"Feature 3 — SpendingScore (Amount x Quantity):\")\n",
    "print(merged[['CustomerID','Amount','Quantity','SpendingScore']].head(10))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "800ea09b-966d-464c-a154-4d6a253a15bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feature 4 — CustomerValue:\n",
      "   CustomerID  SpendingScore CustomerValue\n",
      "0         101        90000.0  Medium Value\n",
      "1         101        16000.0     Low Value\n",
      "2         102        90000.0  Medium Value\n",
      "3         102        55000.0  Medium Value\n",
      "4         103        95000.0  Medium Value\n",
      "5         104       180000.0    High Value\n",
      "6         105            0.0     Low Value\n",
      "7         107       184000.0    High Value\n",
      "8         108            0.0     Low Value\n",
      "9         109            0.0     Low Value\n"
     ]
    }
   ],
   "source": [
    "# ── Feature 4: Customer Value ──\n",
    "def cust_value(score):\n",
    "    if score > 100000:   return 'High Value'\n",
    "    elif score >= 50000: return 'Medium Value'\n",
    "    else:                return 'Low Value'\n",
    "\n",
    "merged['CustomerValue'] = merged['SpendingScore'].apply(cust_value)\n",
    "print(\"Feature 4 — CustomerValue:\")\n",
    "print(merged[['CustomerID','SpendingScore','CustomerValue']].head(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a1e8f725-878d-4e05-a985-1463fe55bdff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feature 5 — PurchaseFrequency:\n",
      "    CustomerID  PurchaseFrequency\n",
      "0          101                  2\n",
      "2          102                  2\n",
      "4          103                  1\n",
      "5          104                  1\n",
      "6          105                  0\n",
      "7          107                  1\n",
      "8          108                  0\n",
      "9          109                  0\n",
      "10         110                  0\n",
      "11         111                  0\n"
     ]
    }
   ],
   "source": [
    "# ── Feature 5: Purchase Frequency ──\n",
    "freq_map = purchases.groupby('CustomerID').size()\n",
    "merged['PurchaseFrequency'] = merged['CustomerID'].map(freq_map).fillna(0).astype(int)\n",
    "print(\"Feature 5 — PurchaseFrequency:\")\n",
    "print(merged[['CustomerID','PurchaseFrequency']].drop_duplicates().head(10))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "45c9f8ab-e1e1-4b4e-b3b5-7cff827c2eef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feature 6 — MembershipDays:\n",
      "    CustomerID   JoinDate  MembershipDays\n",
      "0          101 2024-01-05           886.0\n",
      "2          102 2024-03-12           819.0\n",
      "4          103 2023-11-20           932.0\n",
      "5          104        NaT             NaN\n",
      "6          105 2024-06-01           738.0\n",
      "7          107        NaT             NaN\n",
      "8          108 2023-09-10          1003.0\n",
      "9          109        NaT             NaN\n",
      "10         110        NaT             NaN\n",
      "11         111        NaT             NaN\n"
     ]
    }
   ],
   "source": [
    "# ── Feature 6: Membership Duration ──\n",
    "merged['JoinDate'] = pd.to_datetime(merged['JoinDate'], errors='coerce')\n",
    "merged['MembershipDays'] = (pd.Timestamp.today() - merged['JoinDate']).dt.days\n",
    "print(\"Feature 6 — MembershipDays:\")\n",
    "print(merged[['CustomerID','JoinDate','MembershipDays']].drop_duplicates().head(10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "9d6b43b3-c9e7-4890-b0fc-9f41db93b1e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== ALL NEW FEATURES ===\n",
      "    CustomerID AgeGroup IncomeCategory  SpendingScore CustomerValue  PurchaseFrequency  MembershipDays\n",
      "0          101    Young         Medium        90000.0  Medium Value                  2           886.0\n",
      "1          101    Young         Medium        16000.0     Low Value                  2           886.0\n",
      "2          102    Adult         Medium        90000.0  Medium Value                  2           819.0\n",
      "3          102    Adult         Medium        55000.0  Medium Value                  2           819.0\n",
      "4          103    Adult         Medium        95000.0  Medium Value                  1           932.0\n",
      "5          104    Adult           High       180000.0    High Value                  1             NaN\n",
      "6          105    Adult         Medium            0.0     Low Value                  0           738.0\n",
      "7          107    Adult           High       184000.0    High Value                  1             NaN\n",
      "8          108    Adult         Medium            0.0     Low Value                  0          1003.0\n",
      "9          109   Senior         Medium            0.0     Low Value                  0             NaN\n",
      "10         110    Adult         Medium            0.0     Low Value                  0             NaN\n",
      "11         111    Young            Low            0.0     Low Value                  0             NaN\n",
      "12         112    Adult         Medium            0.0     Low Value                  0             NaN\n",
      "13         113    Adult         Medium            0.0     Low Value                  0             NaN\n",
      "14         114   Senior         Medium            0.0     Low Value                  0             NaN\n",
      "15         115    Young           High            0.0     Low Value                  0             NaN\n",
      "16         116    Adult         Medium            0.0     Low Value                  0             NaN\n",
      "17         117    Adult            Low            0.0     Low Value                  0             NaN\n",
      "18         118    Young           High            0.0     Low Value                  0             NaN\n",
      "19         119    Adult         Medium            0.0     Low Value                  0             NaN\n",
      "20         120    Adult         Medium            0.0     Low Value                  0             NaN\n"
     ]
    }
   ],
   "source": [
    "# All new features together\n",
    "print(\"=== ALL NEW FEATURES ===\")\n",
    "new_features = ['CustomerID','AgeGroup','IncomeCategory','SpendingScore',\n",
    "                'CustomerValue','PurchaseFrequency','MembershipDays']\n",
    "print(merged[new_features].drop_duplicates().to_string())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "057f6021-6952-411e-af52-98dad8bf6f0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Remaining missing values:\n",
      "CustomerID            0\n",
      "Name                  0\n",
      "Age                   0\n",
      "Gender                0\n",
      "City                  0\n",
      "Income                0\n",
      "PurchaseID           14\n",
      "Product              14\n",
      "Quantity             14\n",
      "Amount               14\n",
      "MembershipType       14\n",
      "JoinDate             14\n",
      "AgeGroup              0\n",
      "IncomeCategory        0\n",
      "SpendingScore         0\n",
      "CustomerValue         0\n",
      "PurchaseFrequency     0\n",
      "MembershipDays       14\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# ── Check remaining missing values ──\n",
    "print(\"Remaining missing values:\")\n",
    "print(merged.isnull().sum())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "7b63dd8a-9805-4d0f-b523-17b3fbac998b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ All nulls handled.\n",
      "CustomerID            0\n",
      "Name                  0\n",
      "Age                   0\n",
      "Gender                0\n",
      "City                  0\n",
      "Income                0\n",
      "PurchaseID           14\n",
      "Product              14\n",
      "Quantity              0\n",
      "Amount                0\n",
      "MembershipType        0\n",
      "JoinDate             14\n",
      "AgeGroup              0\n",
      "IncomeCategory        0\n",
      "SpendingScore         0\n",
      "CustomerValue         0\n",
      "PurchaseFrequency     0\n",
      "MembershipDays        0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# ── Fill remaining nulls before encoding ──\n",
    "merged['MembershipType']  = merged['MembershipType'].fillna('None')\n",
    "merged['MembershipDays']  = merged['MembershipDays'].fillna(0)\n",
    "merged['SpendingScore']   = merged['SpendingScore'].fillna(0)\n",
    "merged['Amount']          = merged['Amount'].fillna(0)\n",
    "merged['Quantity']        = merged['Quantity'].fillna(0)\n",
    "\n",
    "print(\"✅ All nulls handled.\")\n",
    "print(merged.isnull().sum())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "c624279f-bbc2-4379-8566-298709c2d591",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Categorical columns encoded.\n",
      "   Gender  City  AgeGroup  IncomeCategory  CustomerValue  MembershipType\n",
      "0       1     2         2               2              2               0\n",
      "1       1     2         2               2              1               0\n",
      "2       0     1         0               2              2               3\n",
      "3       0     1         0               2              2               3\n",
      "4       1     2         0               2              2               2\n"
     ]
    }
   ],
   "source": [
    "# ── Encode categorical columns ──\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "le = LabelEncoder()\n",
    "cat_cols = ['Gender','City','AgeGroup','IncomeCategory','CustomerValue','MembershipType']\n",
    "\n",
    "for col in cat_cols:\n",
    "    merged[col] = le.fit_transform(merged[col].astype(str))\n",
    "\n",
    "print(\"✅ Categorical columns encoded.\")\n",
    "print(merged[cat_cols].head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "a14d29dd-506c-45da-a150-c5d9e29050cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Numeric columns normalized (0 to 1).\n",
      "     Income    Amount  SpendingScore\n",
      "0  0.222222  0.947368       0.489130\n",
      "1  0.222222  0.084211       0.086957\n",
      "2  0.444444  0.473684       0.489130\n",
      "3  0.444444  0.578947       0.298913\n",
      "4  0.346405  1.000000       0.516304\n"
     ]
    }
   ],
   "source": [
    "# ── Normalize numeric columns ──\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "\n",
    "scaler = MinMaxScaler()\n",
    "num_cols = ['Income','Amount','SpendingScore']\n",
    "merged[num_cols] = scaler.fit_transform(merged[num_cols])\n",
    "\n",
    "print(\"✅ Numeric columns normalized (0 to 1).\")\n",
    "print(merged[num_cols].head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "e969b01f-5666-4d92-8faa-369f9866b6f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Dropped Name and PurchaseID.\n",
      "\n",
      "Final DataFrame shape: (21, 16)\n",
      "Final columns: ['CustomerID', 'Age', 'Gender', 'City', 'Income', 'Product', 'Quantity', 'Amount', 'MembershipType', 'JoinDate', 'AgeGroup', 'IncomeCategory', 'SpendingScore', 'CustomerValue', 'PurchaseFrequency', 'MembershipDays']\n"
     ]
    }
   ],
   "source": [
    "# ── Remove irrelevant columns ──\n",
    "merged = merged.drop(columns=['Name','PurchaseID'], errors='ignore')\n",
    "print(\"✅ Dropped Name and PurchaseID.\")\n",
    "\n",
    "# ── Final shape and columns ──\n",
    "print(f\"\\nFinal DataFrame shape: {merged.shape}\")\n",
    "print(f\"Final columns: {merged.columns.tolist()}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "c6642ff1-9973-4d13-b04c-5ab26da72083",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== SAMPLE 20 ROWS ===\n",
      "    CustomerID   Age  Gender  City    Income   Product  Quantity    Amount  MembershipType   JoinDate  AgeGroup  IncomeCategory  SpendingScore  CustomerValue  PurchaseFrequency  MembershipDays\n",
      "12         112  45.0       0     1  0.277778       NaN       0.0  0.000000               1        NaT         0               2       0.000000              1                  0             0.0\n",
      "2          102  33.0       0     1  0.444444     Phone       2.0  0.473684               3 2024-03-12         0               2       0.489130              2                  2           819.0\n",
      "17         117  33.0       1     3  0.000000       NaN       0.0  0.000000               1        NaT         0               1       0.000000              1                  0             0.0\n",
      "11         111  22.0       1     3  0.055556       NaN       0.0  0.000000               1        NaT         2               1       0.000000              1                  0             0.0\n",
      "6          105  33.0       1     1  0.166667       NaN       0.0  0.000000               0 2024-06-01         0               2       0.000000              1                  0           738.0\n",
      "1          101  25.0       1     2  0.222222  Keyboard       2.0  0.084211               0 2024-01-05         2               2       0.086957              1                  2           886.0\n",
      "20         120  33.0       0     2  0.346405       NaN       0.0  0.000000               1        NaT         0               2       0.000000              1                  0             0.0\n",
      "0          101  25.0       1     2  0.222222    Laptop       1.0  0.947368               0 2024-01-05         2               2       0.489130              2                  2           886.0\n",
      "3          102  33.0       0     1  0.444444     Phone       1.0  0.578947               3 2024-03-12         0               2       0.298913              2                  2           819.0\n",
      "16         116  38.0       0     2  0.111111       NaN       0.0  0.000000               1        NaT         0               2       0.000000              1                  0             0.0\n",
      "18         118  26.0       0     1  0.611111       NaN       0.0  0.000000               1        NaT         2               0       0.000000              1                  0             0.0\n",
      "8          108  33.0       0     1  0.388889       NaN       0.0  0.000000               3 2023-09-10         0               2       0.000000              1                  0          1003.0\n",
      "9          109  55.0       1     2  0.346405       NaN       0.0  0.000000               1        NaT         1               2       0.000000              1                  0             0.0\n",
      "7          107  42.0       1     2  1.000000    Laptop       2.0  0.968421               1        NaT         0               0       1.000000              0                  1             0.0\n",
      "14         114  60.0       0     0  0.346405       NaN       0.0  0.000000               1        NaT         1               2       0.000000              1                  0             0.0\n",
      "5          104  35.0       0     0  0.666667    Tablet       3.0  0.631579               1        NaT         0               0       0.978261              0                  1             0.0\n",
      "10         110  31.0       0     0  0.555556       NaN       0.0  0.000000               1        NaT         0               2       0.000000              1                  0             0.0\n",
      "4          103  33.0       1     2  0.346405    Laptop       1.0  1.000000               2 2023-11-20         0               2       0.516304              2                  1           932.0\n",
      "13         113  33.0       1     2  0.500000       NaN       0.0  0.000000               1        NaT         0               2       0.000000              1                  0             0.0\n",
      "19         119  33.0       1     0  0.333333       NaN       0.0  0.000000               1        NaT         0               2       0.000000              1                  0             0.0\n"
     ]
    }
   ],
   "source": [
    "# ── Sample 20 rows ──\n",
    "print(\"=== SAMPLE 20 ROWS ===\")\n",
    "print(merged.sample(min(20, len(merged))).to_string())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "00b9f87e-cfb0-4ec8-b9ba-b3f8a42fe695",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Saved: AI_Ready_Customers.csv\n"
     ]
    }
   ],
   "source": [
    "# ── Save final dataset ──\n",
    "merged.to_csv('AI_Ready_Customers.csv', index=False)\n",
    "print(\"✅ Saved: AI_Ready_Customers.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "bed51e78-4d23-4360-8b99-7c28481f9452",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Reload original merged for analysis (before encoding/scaling)\n",
    "c  = pd.read_csv('customers.csv')\n",
    "p  = pd.read_csv('purchases.csv')\n",
    "m  = pd.read_excel('membership.xlsx', engine='openpyxl')\n",
    "\n",
    "c['Age']    = c['Age'].fillna(c['Age'].median())\n",
    "c['Income'] = c['Income'].fillna(c['Income'].mean())\n",
    "c['City']   = c['City'].fillna('Unknown').str.strip().str.title()\n",
    "c['Gender'] = c['Gender'].fillna('U').str.strip().str.upper()\n",
    "c = c.drop_duplicates()\n",
    "c = c[c['Income'] >= 0].reset_index(drop=True)\n",
    "\n",
    "p['Amount']   = p['Amount'].fillna(p['Amount'].median())\n",
    "p = p.drop_duplicates()\n",
    "p = p[p['Quantity'] > 0].reset_index(drop=True)\n",
    "\n",
    "m['MembershipType'] = m['MembershipType'].fillna('None').str.strip().str.title()\n",
    "\n",
    "anal = pd.merge(c, p, on='CustomerID', how='left')\n",
    "anal = pd.merge(anal, m, on='CustomerID', how='left')\n",
    "anal['SpendingScore'] = anal['Amount'].fillna(0) * anal['Quantity'].fillna(0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "62f2214c-a49b-4923-954e-99c21770ad0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. Top 10 Highest-Spending Customers:\n",
      " CustomerID   Name  SpendingScore\n",
      "        107 Hassan       184000.0\n",
      "        104 Fatima       180000.0\n",
      "        102   Sara       145000.0\n",
      "        101    Ali       106000.0\n",
      "        103  Ahmed        95000.0\n",
      "        105  Usman            0.0\n",
      "        108 Ayesha            0.0\n",
      "        109  Bilal            0.0\n",
      "        110   Hina            0.0\n",
      "        111 Kamran            0.0\n"
     ]
    }
   ],
   "source": [
    "# 1. Top 10 highest-spending customers\n",
    "print(\"1. Top 10 Highest-Spending Customers:\")\n",
    "top10 = anal.groupby(['CustomerID','Name'])['SpendingScore'].sum().nlargest(10).reset_index()\n",
    "print(top10.to_string(index=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "e03a4ebb-cb40-421a-a6a8-18d9a53c819d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2. Customers who never purchased: 14\n",
      " CustomerID   Name\n",
      "        105  Usman\n",
      "        108 Ayesha\n",
      "        109  Bilal\n",
      "        110   Hina\n",
      "        111 Kamran\n",
      "        112   Sana\n",
      "        113  Tariq\n",
      "        114   Nida\n",
      "        115   Asad\n",
      "        116  Rabia\n",
      "        117  Imran\n",
      "        118  Maria\n",
      "        119 Faisal\n",
      "        120   Amna\n"
     ]
    }
   ],
   "source": [
    "# 2. Customers who never purchased\n",
    "never_bought = c[~c['CustomerID'].isin(p['CustomerID'])]\n",
    "print(f\"2. Customers who never purchased: {len(never_bought)}\")\n",
    "print(never_bought[['CustomerID','Name']].to_string(index=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "b584a3a4-e8ae-4020-8455-52f076f8b033",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3. City with Highest Revenue:\n",
      "City\n",
      "Lahore       285000.0\n",
      "Karachi      100000.0\n",
      "Islamabad     60000.0\n",
      "Peshawar          0.0\n",
      "Name: Amount, dtype: float64\n",
      "\n",
      "👑 Top city: Lahore — Rs. 285,000\n"
     ]
    }
   ],
   "source": [
    "# 3. City with highest revenue\n",
    "print(\"3. City with Highest Revenue:\")\n",
    "city_rev = anal.groupby('City')['Amount'].sum().sort_values(ascending=False)\n",
    "print(city_rev)\n",
    "print(f\"\\n👑 Top city: {city_rev.idxmax()} — Rs. {city_rev.max():,.0f}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "c329d7fa-21fd-40eb-bedd-eed690660b6d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4. Most Popular Product:\n",
      "Product\n",
      "Laptop      3\n",
      "Phone       2\n",
      "Tablet      1\n",
      "Keyboard    1\n",
      "Monitor     1\n",
      "Name: count, dtype: int64\n",
      "\n",
      "🏆 Most popular: Laptop\n"
     ]
    }
   ],
   "source": [
    "# 4. Most popular product\n",
    "print(\"4. Most Popular Product:\")\n",
    "print(p['Product'].value_counts())\n",
    "print(f\"\\n🏆 Most popular: {p['Product'].value_counts().idxmax()}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "64da915f-5f38-403d-af20-1b8661e7a00f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5. Customer Ranking by Spending Score:\n",
      " CustomerID   Name  SpendingScore  Rank\n",
      "        107 Hassan       184000.0     1\n",
      "        104 Fatima       180000.0     2\n",
      "        102   Sara        90000.0     3\n",
      "        102   Sara        55000.0     3\n",
      "        101    Ali        90000.0     4\n",
      "        101    Ali        16000.0     4\n",
      "        103  Ahmed        95000.0     5\n",
      "        118  Maria            0.0     6\n",
      "        117  Imran            0.0     6\n",
      "        116  Rabia            0.0     6\n",
      "        115   Asad            0.0     6\n",
      "        114   Nida            0.0     6\n",
      "        113  Tariq            0.0     6\n",
      "        110   Hina            0.0     6\n",
      "        111 Kamran            0.0     6\n"
     ]
    }
   ],
   "source": [
    "# 5. Customer ranking by spending score\n",
    "anal['Rank'] = anal.groupby('CustomerID')['SpendingScore'].transform('sum').rank(ascending=False, method='dense').astype(int)\n",
    "ranking = anal[['CustomerID','Name','SpendingScore','Rank']].drop_duplicates().sort_values('Rank')\n",
    "print(\"5. Customer Ranking by Spending Score:\")\n",
    "print(ranking.head(15).to_string(index=False))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "73925513-f16b-44b9-a4c9-60d7dadf96e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=============================================\n",
      "       📊 DASHBOARD SUMMARY\n",
      "=============================================\n",
      "                    Metric   Value\n",
      "           Total Customers      19\n",
      "           Total Purchases       8\n",
      "       Total Revenue (Rs.) 445,000\n",
      " Avg Customer Income (Rs.)  65,248\n",
      "       Top City by Revenue  Lahore\n",
      "      Most Popular Product  Laptop\n",
      " Customers with Membership       6\n",
      "Customers without Purchase      14\n",
      "=============================================\n"
     ]
    }
   ],
   "source": [
    "# 6. Dashboard Summary Table\n",
    "summary = pd.DataFrame({\n",
    "    'Metric': [\n",
    "        'Total Customers',\n",
    "        'Total Purchases',\n",
    "        'Total Revenue (Rs.)',\n",
    "        'Avg Customer Income (Rs.)',\n",
    "        'Top City by Revenue',\n",
    "        'Most Popular Product',\n",
    "        'Customers with Membership',\n",
    "        'Customers without Purchase'\n",
    "    ],\n",
    "    'Value': [\n",
    "        len(c),\n",
    "        len(p),\n",
    "        f\"{anal['Amount'].sum():,.0f}\",\n",
    "        f\"{c['Income'].mean():,.0f}\",\n",
    "        city_rev.idxmax(),\n",
    "        p['Product'].value_counts().idxmax(),\n",
    "        len(m),\n",
    "        len(never_bought)\n",
    "    ]\n",
    "})\n",
    "print(\"=\" * 45)\n",
    "print(\"       📊 DASHBOARD SUMMARY\")\n",
    "print(\"=\" * 45)\n",
    "print(summary.to_string(index=False))\n",
    "print(\"=\" * 45)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "b9fa9892-6586-437d-9861-3ac5c46b0032",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\WIN11-PRO\\internship\n",
      "['.ipynb_checkpoints', 'AI_Ready_Customers.csv', 'customers.csv', 'Heart Disease Prediction .ipynb', 'Heart_Disease_Prediction.csv', 'House Price Prediction Dataset.csv', 'HousePrice_Prediction.ipynb', 'LabPandas_24PWAI0009.ipynb', 'membership.xlsx', 'Predict Future Stock Prices .ipynb', 'purchases.csv']\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(os.getcwd())        # shows exact folder path\n",
    "print(os.listdir())       # AI_Ready_Customers.csv should appear here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d520671-b7f3-4311-ab38-052098b46599",
   "metadata": {},
   "outputs": [],
   "source": []
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
