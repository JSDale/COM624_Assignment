
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
            this.tabPage2 = new System.Windows.Forms.TabPage();
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.buttonPredict = new System.Windows.Forms.Button();
            this.listBoxInformationSource = new System.Windows.Forms.ListBox();
            this.textBoxEnterTicker = new System.Windows.Forms.TextBox();
            this.richTextBoxPredictions = new System.Windows.Forms.RichTextBox();
            this.tabControlMenu.SuspendLayout();
            this.EnterStockInfoPage.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            this.SuspendLayout();
            // 
            // tabControlMenu
            // 
            this.tabControlMenu.Controls.Add(this.EnterStockInfoPage);
            this.tabControlMenu.Controls.Add(this.tabPage2);
            this.tabControlMenu.Location = new System.Drawing.Point(13, 13);
            this.tabControlMenu.Name = "tabControlMenu";
            this.tabControlMenu.SelectedIndex = 0;
            this.tabControlMenu.Size = new System.Drawing.Size(775, 425);
            this.tabControlMenu.TabIndex = 0;
            // 
            // EnterStockInfoPage
            // 
            this.EnterStockInfoPage.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.EnterStockInfoPage.Controls.Add(this.splitContainer1);
            this.EnterStockInfoPage.Location = new System.Drawing.Point(4, 24);
            this.EnterStockInfoPage.Name = "EnterStockInfoPage";
            this.EnterStockInfoPage.Padding = new System.Windows.Forms.Padding(3);
            this.EnterStockInfoPage.Size = new System.Drawing.Size(767, 397);
            this.EnterStockInfoPage.TabIndex = 0;
            this.EnterStockInfoPage.Text = "Enter Stock To Predict";
            this.EnterStockInfoPage.UseVisualStyleBackColor = true;
            // 
            // tabPage2
            // 
            this.tabPage2.Location = new System.Drawing.Point(4, 24);
            this.tabPage2.Name = "tabPage2";
            this.tabPage2.Padding = new System.Windows.Forms.Padding(3);
            this.tabPage2.Size = new System.Drawing.Size(192, 72);
            this.tabPage2.TabIndex = 1;
            this.tabPage2.Text = "tabPage2";
            this.tabPage2.UseVisualStyleBackColor = true;
            // 
            // splitContainer1
            // 
            this.splitContainer1.Cursor = System.Windows.Forms.Cursors.VSplit;
            this.splitContainer1.Location = new System.Drawing.Point(-1, -1);
            this.splitContainer1.Name = "splitContainer1";
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.buttonPredict);
            this.splitContainer1.Panel1.Controls.Add(this.listBoxInformationSource);
            this.splitContainer1.Panel1.Controls.Add(this.textBoxEnterTicker);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.richTextBoxPredictions);
            this.splitContainer1.Size = new System.Drawing.Size(767, 397);
            this.splitContainer1.SplitterDistance = 255;
            this.splitContainer1.TabIndex = 0;
            // 
            // buttonPredict
            // 
            this.buttonPredict.Location = new System.Drawing.Point(63, 211);
            this.buttonPredict.Name = "buttonPredict";
            this.buttonPredict.Size = new System.Drawing.Size(115, 38);
            this.buttonPredict.TabIndex = 5;
            this.buttonPredict.Text = "Predict";
            this.buttonPredict.UseVisualStyleBackColor = true;
            this.buttonPredict.Click += new System.EventHandler(this.buttonPredict_Click);
            // 
            // listBoxInformationSource
            // 
            this.listBoxInformationSource.FormattingEnabled = true;
            this.listBoxInformationSource.ItemHeight = 15;
            this.listBoxInformationSource.Location = new System.Drawing.Point(7, 171);
            this.listBoxInformationSource.Name = "listBoxInformationSource";
            this.listBoxInformationSource.Size = new System.Drawing.Size(233, 34);
            this.listBoxInformationSource.TabIndex = 4;
            // 
            // textBoxEnterTicker
            // 
            this.textBoxEnterTicker.BackColor = System.Drawing.SystemColors.Window;
            this.textBoxEnterTicker.Location = new System.Drawing.Point(7, 142);
            this.textBoxEnterTicker.Name = "textBoxEnterTicker";
            this.textBoxEnterTicker.Size = new System.Drawing.Size(233, 23);
            this.textBoxEnterTicker.TabIndex = 3;
            this.textBoxEnterTicker.Text = "Enter Stock Ticker";
            // 
            // richTextBoxPredictions
            // 
            this.richTextBoxPredictions.Location = new System.Drawing.Point(3, 0);
            this.richTextBoxPredictions.Name = "richTextBoxPredictions";
            this.richTextBoxPredictions.ReadOnly = true;
            this.richTextBoxPredictions.Size = new System.Drawing.Size(504, 396);
            this.richTextBoxPredictions.TabIndex = 0;
            this.richTextBoxPredictions.Text = "";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
            this.BackColor = System.Drawing.SystemColors.Window;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.tabControlMenu);
            this.Name = "MainForm";
            this.Text = "Stock Preditcting";
            this.tabControlMenu.ResumeLayout(false);
            this.EnterStockInfoPage.ResumeLayout(false);
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel1.PerformLayout();
            this.splitContainer1.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl tabControlMenu;
        private System.Windows.Forms.TabPage EnterStockInfoPage;
        private System.Windows.Forms.TabPage tabPage2;
        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.Button buttonPredict;
        private System.Windows.Forms.ListBox listBoxInformationSource;
        private System.Windows.Forms.TextBox textBoxEnterTicker;
        private System.Windows.Forms.RichTextBox richTextBoxPredictions;
    }
}

