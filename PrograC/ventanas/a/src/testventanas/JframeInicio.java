package testventanas;

import segundaEntrega.vista.IVistaInicio;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import java.awt.GridLayout;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.Font;
import java.awt.event.ActionListener;
import javax.swing.SwingConstants;

public class JframeInicio extends JFrame implements IVistaInicio {

    private static final long serialVersionUID = 1L;
    private JPanel contentPane;
    private JPanel label;
    private JLabel lblQueDesea;
    private JPanel botones;
    private JButton btnBD;
    private JButton btnSim;
    private JLabel lblNewLabel;

    /**
     * Launch the application.
     */
    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    JframeInicio frame = new JframeInicio();
                    frame.setVisible(true);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }

    /**
     * Create the frame.
     */
    public JframeInicio() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 450, 214);
        this.contentPane = new JPanel();
        this.contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(this.contentPane);
        this.contentPane.setLayout(new GridLayout(2, 1, 0, 0));

        this.label = new JPanel();
        this.contentPane.add(this.label);
        this.label.setLayout(new GridLayout(2, 1, 0, 0));

        this.lblQueDesea = new JLabel("Bienvenido al sistema de gestion de la clinica");
        this.lblQueDesea.setHorizontalAlignment(SwingConstants.CENTER);
        this.lblQueDesea.setFont(new Font("Segoe UI", Font.PLAIN, 19));
        this.label.add(this.lblQueDesea);

        this.lblNewLabel = new JLabel(" \u00BF a que modulo desea acceder?");
        this.lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
        this.lblNewLabel.setFont(new Font("Segoe UI", Font.PLAIN, 19));
        this.label.add(this.lblNewLabel);

        this.botones = new JPanel();
        this.contentPane.add(this.botones);

        this.btnBD = new JButton("Modulo base de datos");
        this.btnBD.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        this.botones.add(this.btnBD);

        this.btnSim = new JButton("Modulo de simulacion");
        this.btnSim.setFont(new Font("Segoe UI", Font.PLAIN, 14));
        this.botones.add(this.btnSim);

    }

    @Override
    public void addActionListener(ActionListener l) {
        this.btnBD.addActionListener(l);
        this.btnSim.addActionListener(l);
    }

    @Override
    public void arranca() {
        this.setVisible(true);
    }
    @Override
    public void cerrar() {
        this.dispose();
    }

}
