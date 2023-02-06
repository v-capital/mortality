import pandas as pd 

def validate(input,valid_list):
    if input in valid_list:
        return True

df = pd.read_csv("mortality.csv",index_col=0)


def calc_mort(age,sex):
    if not validate(age,range(1,100)):
        print(f"age={age} is invalid, must be between 1-100.")
        
    if not validate(sex,["M","F"]):
        print(f"sex={sex} is invalid, must be M or F.")

    if sex=="M":
        qx=df["male_qx"].iloc[age]
        le=df["male_le"].iloc[age]
    else:
        qx=df["female_qx"].iloc[age]
        le=df["female_le"].iloc[age]
    
    print(f"A {age} y/o {sex} qx={qx}, life expectancy={le}.")
    return qx,le

if __name__ == "__main__":
    calc_mort(22,"F")
    calc_mort(35,"M")
    