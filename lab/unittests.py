import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import inspect

def test_train_binary_classifier(student_function):
    """
    Test the train_binary_classifier function defined by the student.
    Verifies:
    - Function signature and parameter presence
    - Presence of critical steps: zero_grad, forward, loss, backward, step
    - Correct shape of input and output tensors
    - Proper training loop and loss reduction
    """

    # Step 1: Check function signature
    try:
        sig = inspect.signature(student_function)
        expected_params = ['model', 'dataloader', 'criterion', 'optimizer', 'num_epochs']
        for param in expected_params:
            assert param in sig.parameters, f"Missing parameter: '{param}' in function definition."
    except Exception as e:
        print(f"❌ Function signature test failed: {e}")
        return

    # Step 2: Dummy model for binary classification
    class DummyModel(nn.Module):
        def __init__(self):
            super().__init__()
            self.linear = nn.Linear(2, 1)

        def forward(self, x):
            return self.linear(x)

    # Step 3: Create dummy dataset
    torch.manual_seed(0)
    inputs = torch.randn(20, 2)  # 20 samples, 2 features
    labels = torch.randint(0, 2, (20,))  # Binary labels
    dataset = TensorDataset(inputs, labels)
    dataloader = DataLoader(dataset, batch_size=5)

    model = DummyModel()
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # Step 4: Use hooks to track function calls
    called = {'zero_grad': False, 'step': False, 'backward': False}

    def patched_zero_grad():
        called['zero_grad'] = True
        return original_zero_grad()

    def patched_step():
        called['step'] = True
        return original_step()

    def patched_backward(self):
        called['backward'] = True
        return original_backward(self)

    original_zero_grad = optimizer.zero_grad
    original_step = optimizer.step
    original_backward = torch.Tensor.backward

    optimizer.zero_grad = patched_zero_grad
    optimizer.step = patched_step
    torch.Tensor.backward = patched_backward

    # Step 5: Run function and verify no runtime errors
    try:
        student_function(model, dataloader, criterion, optimizer, num_epochs=2)
    except Exception as e:
        print(f"❌ Runtime error during training: {e}")
        return
    finally:
        # Restore original methods
        optimizer.zero_grad = original_zero_grad
        optimizer.step = original_step
        torch.Tensor.backward = original_backward

    # Step 6: Check calls
    try:
        assert called['zero_grad'], "You haven't reset your gradients."
        assert called['step'], "You haven't implemented the optimizer in your function."
        assert called['backward'], "Backward was not implemented."
    except AssertionError as e:
        print(f"❌ Function call test failed: {e}")
        return

    # Step 7: Check output shapes
    try:
        test_input = torch.randn(1, 2)
        with torch.no_grad():
            output = model(test_input)
        assert output.shape == (1, 1), f"Expected output shape (1, 1), got {output.shape}"
    except Exception as e:
        print(f"❌ Output shape test failed: {e}")
        return

    print("✅ All tests passed! Your training function seems correct. Great job!")