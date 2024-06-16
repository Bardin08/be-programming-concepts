#### Task Description

You need to write a Python application that can manage data sources and calculate metrics. The application should have
the following features:

1. **Main Menu**:
    - When the application starts, the user sees a menu with three options:</br>
      a. Check existing information.</br>
      b. Add a new data source (file).</br>
      c. Calculate metric.</br>

- **Check Existing Information**:
    - The application shows the names of the last three added data sources and their metrics.
      Example:
      ```
      1) Datasource: MicrosoftLTVs2020-2023.csv | Metric: Average LTV = 720$
      2) Datasource: MicrosoftLTVs2015-2019.csv | Metric: Average LTV = 700$
      3) Datasource: MicrosoftLTVs2010-2014.csv | Metric: Average LTV = 550$
      ```

- **Add New Data Source (File)**:
    - The application asks for the path to a new data source file.
      ```
      > Enter data source file path:
      < C://…/datasource.csv
      ```
    - The application displays the structure and total records of the file.
      ```
      > Datasource structure:
        col_1 name | col_2 name | … | col_n name
        Total records: 10256
      ```

- **Calculate Metric**:
    - The user selects a data source from the added ones using keyboard navigation.
      ```
      > Select data source: <- -> (keyboard displays data source name from the added ones)
      Selected data source: datasource.csv | Total records: 10256 records
      ```
    - The application calculates and displays a metric for the selected data source.
      ```
      Based on the dataset was calculated {metric name}
      ```

5. **Return to Main Menu**:
    - After each command, the user is taken back to the main menu.

---

### Functional Requirements

| ID | Description                                                                                                                              |
|----|------------------------------------------------------------------------------------------------------------------------------------------|
| F1 | The application starts with a main menu showing three options: Check existing information, Add new data source (file), Calculate metric. |
| F2 | The application displays the names of the last three added data sources and their metrics.                                               |
| F3 | The application asks the user to enter the file path for a new data source and shows the structure and total records.                    |
| F4 | The application lets the user select a data source using keyboard navigation.                                                            |
| F5 | The application calculates and shows the metric for the selected data source.                                                            |
| F6 | The application returns to the main menu after each command.                                                                             |

### Non-Functional Requirements

| ID  | Description                                                                      |
|-----|----------------------------------------------------------------------------------|
| NF1 | The application should be easy to use and understand.                            |
| NF2 | The application should handle file paths and data structures efficiently.        |
| NF3 | The application should provide clear messages and instructions.                  |
| NF4 | The application should be designed to allow future upgrades and changes.         |
| NF5 | The application should handle errors gracefully and show helpful error messages. |

### Common Use Cases

| Use Case ID | Description                          | Event Flow                                                                                                                                                                                                                                                     |
|-------------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UC1         | Start application and view main menu | 1. User starts the application. <br> 2. Application shows the main menu with options: Check existing information, Add new data source (file), Calculate metric.                                                                                                |
| UC2         | Check existing information           | 1. User selects "Check existing information" from the main menu. <br> 2. Application shows the names of the last three added data sources and their metrics.                                                                                                   |
| UC3         | Add new data source                  | 1. User selects "Add new data source" from the main menu. <br> 2. Application asks for the file path of the new data source. <br> 3. User enters the file path. <br> 4. Application shows the structure and total records of the data source.                  |
| UC4         | Calculate metric                     | 1. User selects "Calculate metric" from the main menu. <br> 2. Application lets the user select a data source using keyboard navigation. <br> 3. User selects a data source. <br> 4. Application calculates and shows the metric for the selected data source. |
| UC5         | Return to main menu after a command  | 1. After executing any command, the application takes the user back to the main menu.                                                                                                                                                                          |

---

### Notes

- **Metric Variants**: The metric calculated depends on the variant assigned to each student. Ask your instructor for
  details on the specific metric you need to calculate.
- **Data Source Files**: The data source files are CSV files with a specific structure. The application should be 
  able to read and process these files.
- **Data Source Structure**: The structure of the data source files is predefined for each variant. The application 
  should display the structure of the data source files when a new file is added.
- **Data Source Metrics**: The metrics are calculated based on the data in the data source files. The application 
  should be able to calculate and display the metrics for each data source.