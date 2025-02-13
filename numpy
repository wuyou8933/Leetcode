import pandas as pd

input_file = "Prediction_Cum_Roll_Rate-wECOE.xlsx"  # Source file
output_file = "Roll_Rate_Multiply.xlsx"  # Destination file

# Read all sheets from the Excel file
excel_data = pd.read_excel(input_file, sheet_name=None)

# Create a writer object for the output file
writer = pd.ExcelWriter(output_file, engine="xlsxwriter")

# Process each sheet separately
for sheet_name, period_data in excel_data.items():
    # Ensure all columns except the first one are numeric
    period_data.iloc[:, 1:] = period_data.iloc[:, 1:].apply(pd.to_numeric, errors="coerce")

    # Create DataFrames for Actual, Prediction, and Difference
    actual_df = period_data.copy()
    prediction_df = period_data.copy()
    difference_df = period_data.copy()

    # Compute difference (assuming column-wise calculations)
    prediction_df.iloc[:, 1:] = actual_df.iloc[:, 1:]  # You may update with actual predictions
    difference_df.iloc[:, 1:] = actual_df.iloc[:, 1:] - prediction_df.iloc[:, 1:]

    # Ensure sheet names are formatted correctly
    try:
        month_number = sheet_name.split("_")[1]
    except IndexError:
        month_number = sheet_name  # Fallback if split fails

    formatted_sheet_name = f"Month{month_number}"

    # Write processed data to the output file
    period_data.to_excel(writer, sheet_name=formatted_sheet_name, startrow=0, startcol=0, index=False)
    prediction_df.to_excel(writer, sheet_name=formatted_sheet_name, startrow=0, startcol=len(period_data.columns) + 2, index=False)
    difference_df.to_excel(writer, sheet_name=formatted_sheet_name, startrow=0, startcol=2 * (len(period_data.columns) + 2), index=False)

# Save the output Excel file
writer.save()

print("Data has been successfully processed and saved.")