import streamlit as st
from io import BytesIO
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill
from openpyxl.utils import get_column_letter

def process_prediction_data(prediction_data, city):
    try:
        # Create an Excel file in memory
        output = BytesIO()
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        worksheet.title = "Predicciones"

        # Write headers
        headers = list(prediction_data.columns)
        for col, header in enumerate(headers, start=1):
            cell = worksheet.cell(row=1, column=col, value=header)
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
            cell.alignment = Alignment(horizontal="center", vertical="center")

        # Write data
        for row, data in enumerate(prediction_data.values, start=2):
            for col, value in enumerate(data, start=1):
                cell = worksheet.cell(row=row, column=col, value=value)
                cell.alignment = Alignment(horizontal="center")

        # Adjust column widths
        for column in worksheet.columns:
            max_length = 0
            column_letter = get_column_letter(column[0].column)
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2)
            worksheet.column_dimensions[column_letter].width = adjusted_width

        # Save the workbook to the BytesIO object
        workbook.save(output)
        output.seek(0)

        # Create download button
        st.download_button(
            label="Descargar predicción en Excel",
            data=output,
            file_name=f"{city}_prediccion.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"Error al preparar el archivo para descarga: {str(e)}")

