
namespace CustomEvents
{
    /// <summary>
    /// The event to use when an error message should be displayed.
    /// </summary>
    public class CustomDisplayError
    {
        /// <summary>
        /// delegate for passing stock predictions to GUI
        /// </summary>
        /// <param name="errorMessage">The predictions to pass</param>
        public delegate void DisplayError(string errorMessage);

        /// <summary>
        /// Event to handle when stock predictions are published
        /// </summary>
        public static event DisplayError DisplayErrorEvent;

        /// <summary>
        /// Invokes the <see cref="UpdateStockEvent"/>.
        /// </summary>
        /// <param name="errorMessage">the predictions to pass to GUI</param>
        public static void InvokeDisplayError(string errorMessage)
        {
            DisplayErrorEvent.Invoke(errorMessage);
        }
    }
}
