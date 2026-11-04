import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# 1. PREPARE THE DATA
# Imagine features: [Square Footage / 100, Number of Bedrooms]
# Imagine target: [House Price in thousands of dollars]
features = torch.tensor([
    [15.0, 2.0], [20.0, 3.0], [12.0, 2.0], [30.0, 4.0], 
    [25.0, 3.0], [18.0, 3.0], [10.0, 1.0], [35.0, 5.0]
], dtype=torch.float32)

prices = torch.tensor([
    [250.0], [320.0], [210.0], [450.0], 
    [380.0], [290.0], [150.0], [520.0]
], dtype=torch.float32)

# Wrap data into a standard PyTorch Dataset and Loader for batch processing
dataset = TensorDataset(features, prices)
data_loader = DataLoader(dataset, batch_size=2, shuffle=True)


# 2. DESIGN THE ARCHITECTURE
# We create a simple network that accepts 2 inputs and outputs 1 prediction
class HousePriceModel(nn.Module):
    def __init__(self):
        super(HousePriceModel, self).__init__()
        self.layer1 = nn.Linear(2, 4)  # Hidden layer: accepts 2 inputs, outputs 4 features
        self.relu = nn.ReLU()          # Activation function: introduces non-linearity
        self.layer2 = nn.Linear(4, 1)  # Output layer: takes 4 features, outputs 1 price

    def forward(self, x):
        # Defines how data flows forward through the network
        x = self.relu(self.layer1(x))
        x = self.layer2(x)
        return x

# Initialize the model
model = HousePriceModel()


# 3. CHOOSE MATH SETTINGS
criterion = nn.MSELoss()  # Mean Squared Error Loss: Perfect for predicting continuous values
optimizer = optim.SGD(model.parameters(), lr=0.001)  # Stochastic Gradient Descent


# 4. TRAIN THE MODEL
print("--- Starting Training Loop ---")
for epoch in range(200):
    epoch_loss = 0.0
    
    # Process the data in the small batches we set up in step 1
    for batch_features, batch_prices in data_loader:
        # Clear past math calculations
        optimizer.zero_grad()
        
        # Make a guess
        predictions = model(batch_features)
        
        # Calculate how wrong the guess was
        loss = criterion(predictions, batch_prices)
        
        # Calculate gradients (backpropagation)
        loss.backward()
        
        # Adjust the model's weights based on the loss
        optimizer.step()
        
        epoch_loss += loss.item()
        
    # Print status updates every 40 rounds
    if (epoch + 1) % 40 == 0:
        average_loss = epoch_loss / len(data_loader)
        print(f"Epoch [{epoch+1}/200] | Avg Loss: {average_loss:.2f}")


# 5. TEST THE MODEL ON A NEW HOUSE
model.eval()  # Put model in evaluation mode
with torch.no_grad():  # Turn off engine tracking to save system memory
    # A new house: 2,200 sq ft (22.0) with 3 bedrooms (3.0)
    new_house = torch.tensor([[22.0, 3.0]], dtype=torch.float32)
    predicted_price = model(new_house)
    print(f"\nPredicted price for a 2,200 sq ft, 3-bed house: ${predicted_price.item() * 1000:.2f}")
