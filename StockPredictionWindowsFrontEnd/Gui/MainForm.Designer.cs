
namespace Gui
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.tabControlMenu = new System.Windows.Forms.TabControl();
            this.EnterStockInfoPage = new System.Windows.Forms.TabPage();
            this.panel1 = new System.Windows.Forms.Panel();
            this.comboBoxModelType = new System.Windows.Forms.ComboBox();
            this.richTextBoxPredictions = new System.Windows.Forms.RichTextBox();
            this.comboBoxInfoSource = new System.Windows.Forms.ComboBox();
            this.buttonPredict = new System.Windows.Forms.Button();
            this.textBoxEnterTicker = new System.Windows.Forms.TextBox();
            this.tabPageGraph = new System.Windows.Forms.TabPage();
            this.pictureBoxGraph = new System.Windows.Forms.PictureBox();
            this.tabPageConfiguration = new System.Windows.Forms.TabPage();
            this.labelPassword = new System.Windows.Forms.Label();
            this.textBoxPassword = new System.Windows.Forms.TextBox();
            this.labelUsername = new System.Windows.Forms.Label();
            this.textBoxUsername = new System.Windows.Forms.TextBox();
            this.buttonApplyConfig = new System.Windows.Forms.Button();
            this.labelHostname = new System.Windows.Forms.Label();
            this.textBoxHostname = new System.Windows.Forms.TextBox();
            this.tabControlMenu.SuspendLayout();
            this.EnterStockInfoPage.SuspendLayout();
            this.panel1.SuspendLayout();
            this.tabPageGraph.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxGraph)).BeginInit();
            this.tabPageConfiguration.SuspendLayout();
            this.SuspendLayout();
            // 
            // tabControlMenu
            // 
            this.tabControlMenu.Alignment = System.Windows.Forms.TabAlignment.Bottom;
            this.tabControlMenu.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tabControlMenu.Controls.Add(this.EnterStockInfoPage);
            this.tabControlMenu.Controls.Add(this.tabPageGraph);
            this.tabControlMenu.Controls.Add(this.tabPageConfiguration);
            this.tabControlMenu.Location = new System.Drawing.Point(0, 0);
            this.tabControlMenu.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.tabControlMenu.Name = "tabControlMenu";
            this.tabControlMenu.SelectedIndex = 0;
            this.tabControlMenu.Size = new System.Drawing.Size(968, 600);
            this.tabControlMenu.TabIndex = 0;
            // 
            // EnterStockInfoPage
            // 
            this.EnterStockInfoPage.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.EnterStockInfoPage.Controls.Add(this.panel1);
            this.EnterStockInfoPage.Location = new System.Drawing.Point(4, 4);
            this.EnterStockInfoPage.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.EnterStockInfoPage.Name = "EnterStockInfoPage";
            this.EnterStockInfoPage.Padding = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.EnterStockInfoPage.Size = new System.Drawing.Size(960, 567);
            this.EnterStockInfoPage.TabIndex = 0;
            this.EnterStockInfoPage.Text = "Enter Stock To Predict";
            this.EnterStockInfoPage.UseVisualStyleBackColor = true;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.comboBoxModelType);
            this.panel1.Controls.Add(this.richTextBoxPredictions);
            this.panel1.Controls.Add(this.comboBoxInfoSource);
            this.panel1.Controls.Add(this.buttonPredict);
            this.panel1.Controls.Add(this.textBoxEnterTicker);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel1.Location = new System.Drawing.Point(3, 4);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(952, 557);
            this.panel1.TabIndex = 0;
            // 
            // comboBoxModelType
            // 
            this.comboBoxModelType.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxModelType.FormattingEnabled = true;
            this.comboBoxModelType.Items.AddRange(new object[] {
            "linear regression",
            "polynomial regression 2d",
            "polynomial regression 3d",
            "k nearest neighbour"});
            this.comboBoxModelType.Location = new System.Drawing.Point(42, 165);
            this.comboBoxModelType.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.comboBoxModelType.Name = "comboBoxModelType";
            this.comboBoxModelType.Size = new System.Drawing.Size(266, 28);
            this.comboBoxModelType.TabIndex = 11;
            // 
            // richTextBoxPredictions
            // 
            this.richTextBoxPredictions.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.richTextBoxPredictions.Location = new System.Drawing.Point(365, 0);
            this.richTextBoxPredictions.Name = "richTextBoxPredictions";
            this.richTextBoxPredictions.ReadOnly = true;
            this.richTextBoxPredictions.Size = new System.Drawing.Size(587, 557);
            this.richTextBoxPredictions.TabIndex = 10;
            this.richTextBoxPredictions.Text = "";
            // 
            // comboBoxInfoSource
            // 
            this.comboBoxInfoSource.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboBoxInfoSource.FormattingEnabled = true;
            this.comboBoxInfoSource.Items.AddRange(new object[] {
            "yahoo"});
            this.comboBoxInfoSource.Location = new System.Drawing.Point(42, 240);
            this.comboBoxInfoSource.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.comboBoxInfoSource.Name = "comboBoxInfoSource";
            this.comboBoxInfoSource.Size = new System.Drawing.Size(266, 28);
            this.comboBoxInfoSource.TabIndex = 9;
            // 
            // buttonPredict
            // 
            this.buttonPredict.Location = new System.Drawing.Point(106, 293);
            this.buttonPredict.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.buttonPredict.Name = "buttonPredict";
            this.buttonPredict.Size = new System.Drawing.Size(131, 51);
            this.buttonPredict.TabIndex = 8;
            this.buttonPredict.Text = "Predict";
            this.buttonPredict.UseVisualStyleBackColor = true;
            this.buttonPredict.Click += new System.EventHandler(this.buttonPredict_Click);
            // 
            // textBoxEnterTicker
            // 
            this.textBoxEnterTicker.BackColor = System.Drawing.SystemColors.Window;
            this.textBoxEnterTicker.Location = new System.Drawing.Point(42, 201);
            this.textBoxEnterTicker.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.textBoxEnterTicker.Name = "textBoxEnterTicker";
            this.textBoxEnterTicker.Size = new System.Drawing.Size(266, 27);
            this.textBoxEnterTicker.TabIndex = 7;
            this.textBoxEnterTicker.Text = "Enter Stock Ticker";
            // 
            // tabPageGraph
            // 
            this.tabPageGraph.Controls.Add(this.pictureBoxGraph);
            this.tabPageGraph.Location = new System.Drawing.Point(4, 4);
            this.tabPageGraph.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.tabPageGraph.Name = "tabPageGraph";
            this.tabPageGraph.Padding = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.tabPageGraph.Size = new System.Drawing.Size(960, 567);
            this.tabPageGraph.TabIndex = 1;
            this.tabPageGraph.Text = "Prediction Graph";
            this.tabPageGraph.UseVisualStyleBackColor = true;
            // 
            // pictureBoxGraph
            // 
            this.pictureBoxGraph.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxGraph.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pictureBoxGraph.Location = new System.Drawing.Point(3, 4);
            this.pictureBoxGraph.Name = "pictureBoxGraph";
            this.pictureBoxGraph.Size = new System.Drawing.Size(954, 559);
            this.pictureBoxGraph.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBoxGraph.TabIndex = 0;
            this.pictureBoxGraph.TabStop = false;
            // 
            // tabPageConfiguration
            // 
            this.tabPageConfiguration.Controls.Add(this.labelPassword);
            this.tabPageConfiguration.Controls.Add(this.textBoxPassword);
            this.tabPageConfiguration.Controls.Add(this.labelUsername);
            this.tabPageConfiguration.Controls.Add(this.textBoxUsername);
            this.tabPageConfiguration.Controls.Add(this.buttonApplyConfig);
            this.tabPageConfiguration.Controls.Add(this.labelHostname);
            this.tabPageConfiguration.Controls.Add(this.textBoxHostname);
            this.tabPageConfiguration.Location = new System.Drawing.Point(4, 4);
            this.tabPageConfiguration.Name = "tabPageConfiguration";
            this.tabPageConfiguration.Padding = new System.Windows.Forms.Padding(3);
            this.tabPageConfiguration.Size = new System.Drawing.Size(960, 567);
            this.tabPageConfiguration.TabIndex = 2;
            this.tabPageConfiguration.Text = "Configuration";
            this.tabPageConfiguration.UseVisualStyleBackColor = true;
            // 
            // labelPassword
            // 
            this.labelPassword.AutoSize = true;
            this.labelPassword.Location = new System.Drawing.Point(60, 189);
            this.labelPassword.Name = "labelPassword";
            this.labelPassword.Size = new System.Drawing.Size(70, 20);
            this.labelPassword.TabIndex = 6;
            this.labelPassword.Text = "Password";
            // 
            // textBoxPassword
            // 
            this.textBoxPassword.Location = new System.Drawing.Point(60, 220);
            this.textBoxPassword.Name = "textBoxPassword";
            this.textBoxPassword.Size = new System.Drawing.Size(125, 27);
            this.textBoxPassword.TabIndex = 5;
            this.textBoxPassword.Text = "guest";
            // 
            // labelUsername
            // 
            this.labelUsername.AutoSize = true;
            this.labelUsername.Location = new System.Drawing.Point(60, 112);
            this.labelUsername.Name = "labelUsername";
            this.labelUsername.Size = new System.Drawing.Size(75, 20);
            this.labelUsername.TabIndex = 4;
            this.labelUsername.Text = "Username";
            // 
            // textBoxUsername
            // 
            this.textBoxUsername.Location = new System.Drawing.Point(60, 143);
            this.textBoxUsername.Name = "textBoxUsername";
            this.textBoxUsername.Size = new System.Drawing.Size(125, 27);
            this.textBoxUsername.TabIndex = 3;
            this.textBoxUsername.Text = "guest";
            // 
            // buttonApplyConfig
            // 
            this.buttonApplyConfig.Location = new System.Drawing.Point(409, 532);
            this.buttonApplyConfig.Name = "buttonApplyConfig";
            this.buttonApplyConfig.Size = new System.Drawing.Size(120, 29);
            this.buttonApplyConfig.TabIndex = 2;
            this.buttonApplyConfig.Text = "Apply";
            this.buttonApplyConfig.UseVisualStyleBackColor = true;
            this.buttonApplyConfig.Click += new System.EventHandler(this.buttonApplyConfig_Click);
            // 
            // labelHostname
            // 
            this.labelHostname.AutoSize = true;
            this.labelHostname.Location = new System.Drawing.Point(60, 36);
            this.labelHostname.Name = "labelHostname";
            this.labelHostname.Size = new System.Drawing.Size(77, 20);
            this.labelHostname.TabIndex = 1;
            this.labelHostname.Text = "Hostname";
            // 
            // textBoxHostname
            // 
            this.textBoxHostname.Location = new System.Drawing.Point(60, 67);
            this.textBoxHostname.Name = "textBoxHostname";
            this.textBoxHostname.Size = new System.Drawing.Size(125, 27);
            this.textBoxHostname.TabIndex = 0;
            this.textBoxHostname.Text = "localhost";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Window;
            this.ClientSize = new System.Drawing.Size(967, 600);
            this.Controls.Add(this.tabControlMenu);
            this.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.MinimumSize = new System.Drawing.Size(932, 647);
            this.Name = "MainForm";
            this.Text = "Stock Preditcting";
            this.tabControlMenu.ResumeLayout(false);
            this.EnterStockInfoPage.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.tabPageGraph.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxGraph)).EndInit();
            this.tabPageConfiguration.ResumeLayout(false);
            this.tabPageConfiguration.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl tabControlMenu;
        private System.Windows.Forms.TabPage EnterStockInfoPage;
        private System.Windows.Forms.TabPage tabPageGraph;
        private System.Windows.Forms.PictureBox pictureBoxGraph;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.RichTextBox richTextBoxPredictions;
        private System.Windows.Forms.ComboBox comboBoxInfoSource;
        private System.Windows.Forms.Button buttonPredict;
        private System.Windows.Forms.TextBox textBoxEnterTicker;
        private System.Windows.Forms.ComboBox comboBoxModelType;
        private System.Windows.Forms.TabPage tabPageConfiguration;
        private System.Windows.Forms.Label labelHostname;
        private System.Windows.Forms.TextBox textBoxHostname;
        private System.Windows.Forms.Label labelPassword;
        private System.Windows.Forms.TextBox textBoxPassword;
        private System.Windows.Forms.Label labelUsername;
        private System.Windows.Forms.TextBox textBoxUsername;
        private System.Windows.Forms.Button buttonApplyConfig;
    }
}

