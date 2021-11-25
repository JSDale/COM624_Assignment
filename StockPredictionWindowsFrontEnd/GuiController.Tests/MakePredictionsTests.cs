

namespace GuiController.Tests
{
    using Xunit;

    /// <summary>
    /// Tests getting the predictions.
    /// </summary>
    public class MakePredictionsTests
    {
        [Fact]
        public void Test1()
        {
            var controller = new MakePredictions("AAPL", "yahoo", "linear");
            controller.GetPredictions();
        }
    }
}
