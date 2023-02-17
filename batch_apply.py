import pandas as pd

def batch_apply(func,args:pd.DataFrame):
    success = []
    message  = []
    for entry in args.iterrows():
        try:
            func(**entry[1])
            success.append(True)
            message.append("")
        except Exception as e:
            success.append(False)
            message.append(str(e))
    args["BATCH_SUCCESS"] = pd.Series(success)
    args["BATCH_MESSAGE"] = pd.Series(message)
    return None
