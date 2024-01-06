import controlP5.*;

ControlP5 cp5;
Textfield quotaField, soldScrapValueField, daysUntilDeadlineField;
Textfield[] fields;
float quota = 0;
float soldScrapValue = 0;
int daysUntilDeadline = 0;
float overtimeBonus = 0;
int activeField = 0;

void setup() {
  size(500, 220);
  textSize(16);
  cp5 = new ControlP5(this);
  
  // Define a green color for text
  int green = color(0, 255, 0);
  
  // Create text fields without linking them directly to variables
  quotaField = cp5.addTextfield("Quota")
                 .setPosition(180, 40)
                 .setSize(160, 20)
                 .setColorValue(green)
                 .setAutoClear(false);
  
  soldScrapValueField = cp5.addTextfield("Sold Scrap Value")
                           .setPosition(180, 70)
                           .setSize(160, 20)
                           .setColorValue(green)
                           .setAutoClear(false);
  
  daysUntilDeadlineField = cp5.addTextfield("Days until Deadline")
                              .setPosition(180, 100)
                              .setSize(160, 20)
                              .setColorValue(green)
                              .setAutoClear(false)
                              .setText("0");  // Default value set to 0
  
  fields = new Textfield[] {quotaField, soldScrapValueField, daysUntilDeadlineField};
  fields[activeField].setFocus(true);
}

void draw() {
  background(255);
  fill(0);
  text("Press Enter after typing to calculate Overtime Bonus", 20, 20);
  
  // Display labels for text fields
  text("Quota:", 20, 55);
  text("Sold Scrap Value:", 20, 85);
  text("Days until Deadline:", 20, 115);
  
  text("Overtime Bonus: " + int(overtimeBonus), 20, 190); // Display as an integer
}

void keyPressed() {
  if (key == ENTER || key == RETURN) {
    calculateAndDisplayOvertimeBonus();
  } else if (key == TAB) {
    focusNext(); // Focus the next text field
    key = CODED; // Suppress the default tab behavior
  }
}

void focusNext() {
  activeField = (activeField + 1) % fields.length;
  for (Textfield field : fields) {
    field.setFocus(false);
  }
  fields[activeField].setFocus(true);
}

void calculateAndDisplayOvertimeBonus() {
  try {
    // Parse values manually from the text fields
    quota = quotaField.getText().equals("") ? 0 : Float.parseFloat(quotaField.getText());
    soldScrapValue = soldScrapValueField.getText().equals("") ? 0 : Float.parseFloat(soldScrapValueField.getText());
    daysUntilDeadline = daysUntilDeadlineField.getText().equals("") ? 0 : Integer.parseInt(daysUntilDeadlineField.getText());
    overtimeBonus = (soldScrapValue - quota) / 5 + 15 * (daysUntilDeadline - 1);
  } catch(Exception e) {
    overtimeBonus = 0; // Reset if there's an error in parsing
  }
  
  // Ensure the overtime bonus is not negative and round down
  overtimeBonus = max(overtimeBonus, 0);
  overtimeBonus = floor(overtimeBonus);
}
