# Spring '21 locators
outboundfundsnpsp_lex_locators = {
    "app_launcher": {
        "view_all_button": "//button[text()='View All']",
        "app_link": "//p[contains(@title,'{}')]",
        "app_link_search_result": "//mark[contains(text(),'{}')]",
        "search_input": "//input[contains(@placeholder,'Search apps or items...')]",
    },
    "new_record": {
        "label": "//label[text()='{}']",
        "title": "//h2[contains(@class, 'inlineTitle') and text()='{}']",
        "field_label": "//div[./*/*[text()='{}']]",
        "edit_title": "//h2[contains(@class, 'title') and text()='{}']",
        "list": "//div[contains(@class,'forcePageBlockSectionRow')]/div[contains(@class,'forcePageBlockItem')]/div[contains(@class,'slds-hint-parent')]/div[@class='slds-form-element__control']/div[.//span[text()='{}']][//div[contains(@class,'uiMenu')]//a[@class='select']]",
        "text_field": "//div[contains(@class, 'uiInput')][.//label[contains(@class, 'uiLabel')][.//span[text()='{}']]]//*[self::input or self::textarea]",
        "dropdown_field": "//lightning-combobox[./label[text()='{}']]/div//input[contains(@class,'combobox__input')]",
        "dropdown_popup": "//div[contains(@class, 'slds-dropdown-trigger')]/div[contains(@class, 'slds-listbox')]",
        "dropdown_value": "//div[contains(@class,'slds-listbox')]//lightning-base-combobox-item//span[text()='{}']",
        "dd_selection": "//lightning-base-combobox-item[@data-value='{}']",
        "button": "//button[contains(@class, 'slds-button')  and text()='{}']",
        "lookup_field": "//div[contains(@class, 'autocompleteWrapper')]//input[@title='{}']",
        "lightning_lookup": "//label[text()='{}']/following-sibling::div//input",
        "lookup_value": "//div[contains(@class, 'listContent')]//div[contains(@class, 'slds-truncate') and @title='{}']",
        "checkbox": "//div[contains(@class,'uiInputCheckbox')]/label/span[text()='{}']/../following-sibling::input[@type='checkbox']",
        "field_input": '//label[text()="{}"]/following-sibling::div//*[self::input or self::textarea]',
        "date_field": "//div[contains(@class,'slds-dropdown-trigger')][./label[text()='{}']]/div/input",
        "select_date": "//div[contains(@class,'uiDatePickerGrid')]/table[@class='calGrid']//*[text()='{}']",
        "text-field": "//label/span[text()='{}']/../following-sibling::input",
        "footer_button": "//lightning-button//button[text()='{}']",
    },
    "confirm": {
        "check_value": "//div[contains(@class, 'forcePageBlockItem') or contains(@class, 'slds-form-element_stacked')][.//span[text()='{}']]//following-sibling::div[.//span[contains(@class, 'test-id__field-value')]]//*[text()='{}']",
        "check_status": "//div[contains(@class, 'field-label-container')][.//span[text()='{}']]//following-sibling::div[.//span[contains(@class, 'test-id__field-value')]]/span//lightning-formatted-text[text()='{}']",
        "check_numbers": "//div[contains(@class, 'field-label-container')][.//span[text()='{}']]//following-sibling::div[.//span[contains(@class, 'test-id__field-value')]]/span//lightning-formatted-number[text()='{}']",
    },
    "tab": {
        "tab_header": "//a[@class='slds-tabs_default__link' and text()='{}']",
        "record_detail_tab": "//a[contains(@data-label,'{}')]",
        "verify_header": "//div[contains(@class, 'entityNameTitle')]",
        "verify_details": "//div[contains(@class, 'slds-form-element')][.//span[text()='{}']]//following-sibling::div[.//span[contains(@class, 'test-id__field-value')]]/span",
    },
    "related": {
        "title": '//div[contains(@class, "slds-card")]/header[.//span[@title="{}"]]',
        "button": "//div[contains(@class, 'forceRelatedListSingleContainer')][.//img][.//span[@title='{}']]//a[@title='{}']",
        "count": "//tbody/tr/td[1]",
        "flexi_button": "//div[@lst-listviewmanagerheader_listviewmanagerheader][.//span[@title='{}']]//lightning-button//button[text()='{}']",
        "flexi_link": "//a//span[contains(text(),'{}')]",
    },
    "details": {
        "button": "//button[contains(@class, 'slds-button') and text() = '{}']",
        "header": "//h1//div[contains(@class, 'entityNameTitle') and contains(text(),'{}')]",
    },
    "link": "//a[contains(text(),'{}')]",
}
