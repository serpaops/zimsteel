# Odoo Invoice Template Customization for ZIMSTEEL (XML Only)

This repository contains an Odoo custom module that modifies the standard invoice template using **only XML**, avoiding any Python code. This approach allows for simpler deployments and easier maintenance for basic template adjustments.

## Features

*   Customized invoice template without Python code.
*   Modifications implemented through QWeb views (XML).
*   Easily adaptable to different Odoo versions (within reasonable compatibility ranges).
*   Focus on structural and stylistic changes; for complex logic, Python remains necessary.

## Installation

1.  Clone this repository into your Odoo addons path:

    ```bash
    git clone https://github.com/serpaops/zimsteel
    ```

2.  Ensure the module directory is within your Odoo addons path. You can configure this in your Odoo configuration file (`odoo.conf`). Example:

    ```
    addons_path = /path/to/odoo/addons,/path/to/your/custom/addons
    ```

3.  Restart your Odoo service.

4.  In Odoo, navigate to Apps and update the Apps list.

5.  Search for and install the module named `your_module_technical_name` (usually the same as the repository name or the module's manifest name).

## Usage

After installation, the customized invoice template will be automatically applied when printing or generating invoices. No further configuration is required.

## Customization

To further customize the template, you'll need to modify the XML views within the module.

*   **Key Files:**
    *   `views/report_invoice_document.xml`: This file contains the QWeb view definition for the invoice template. This is where you'll make most of your changes.

*   **Example Modifications (within `views/report_invoice_document.xml`):**

    *   **Adding a custom header:**

        ```xml
        <t t-name="account.report_invoice_document">
            <div class="header">
                <p>My Custom Invoice Header</p>
            </div>
            ...
        </t>
        ```

    *   **Changing styling:**

        ```xml
        <t t-name="account.report_invoice_document">
            <div class="page">
                <div style="font-family: 'Arial';">
                    ...
                </div>
            </div>
        </t>
        ```

    *   **Adding or moving existing fields:**

        Inspect the original Odoo invoice template (in the `account.move` module) to find the XPath of the elements you want to modify. Then, use XPath expressions to target those elements in your custom view.

## Limitations

*   This approach is best suited for visual and structural changes.
*   Complex logic, calculations, or data manipulation require Python code.
*   Upgrading to significantly different Odoo versions might require adjustments to the XML views due to potential template changes in the core Odoo modules.

## Technical Details

*   **Module Technical Name:** `zimsteel` (replace with your module's actual technical name)
*   **Dependencies:** `account.move` (the base module for accounting and invoices)

## Contributing

Contributions are welcome! If you find bugs or have improvements, please submit a pull request.

## License

[Specify your license here, e.g., LGPL-3 or MIT]

## Contact

[Your Name/Email Address (Optional)]