

namespace Gui
{
    using System.Diagnostics.CodeAnalysis;
    using System.Windows.Forms;

    /// <summary>
    /// The main form for the application
    /// </summary>
    public partial class MainForm : Form
    {
        /// <summary>
        /// Creates the main form for the application
        /// </summary>
        public MainForm()
        {
            this. InitializeComponent();
        }

        /// <summary>
        /// Hooks onto buttonPredict click event
        /// </summary>
        /// <param name="sender">The context</param>
        /// <param name="e">event arguments</param>
        [SuppressMessage("StyleCop.CSharp.NamingRules", "SA1300:ElementMustBeginWithUpperCaseLetter", Justification = "Reviewed. Suppression is OK here.")]
        private void buttonPredict_Click(object sender, System.EventArgs e)
        {

        }
    }
}
