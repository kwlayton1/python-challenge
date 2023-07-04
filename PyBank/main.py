{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ed8f77a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-10</td>\n",
       "      <td>1088983</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-10</td>\n",
       "      <td>-354534</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-10</td>\n",
       "      <td>276622</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-10</td>\n",
       "      <td>-728133</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-10</td>\n",
       "      <td>852993</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date  Profit/Losses\n",
       "0  Jan-10        1088983\n",
       "1  Feb-10        -354534\n",
       "2  Mar-10         276622\n",
       "3  Apr-10        -728133\n",
       "4  May-10         852993"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#import pandas\n",
    "import pandas as pd\n",
    "\n",
    "#read csv file\n",
    "df = pd.read_csv(r\"C:\\Users\\kwlay\\python-challenge\\PyBank\\Resources\\budget_data.csv\")\n",
    "\n",
    "#check file load\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "200183eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(86, 2)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#counts total number of months - number of rows in column 1\n",
    "df.shape\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.10.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
