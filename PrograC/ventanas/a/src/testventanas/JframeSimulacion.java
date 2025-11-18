package segundaEntrega.vista;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JTextArea;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;
import java.awt.Insets;
import javax.swing.border.TitledBorder;
import java.awt.Font;
import java.awt.event.ActionListener;
import javax.swing.JTextField;
import javax.swing.SwingConstants;
import javax.swing.JScrollPane;
import java.awt.FlowLayout;
import java.awt.BorderLayout;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class JframeSimulacion extends JFrame implements IVistaSimulacion, KeyListener {

    private static final long serialVersionUID = 1L;
    private JPanel contentPane;
    private JPanel Principal;
    private JPanel movimientosAsociado;
    private JTextArea txtAsociado;
    private JPanel panel;
    private JPanel operario;
    private JPanel estadoAmbulancia;
    private JPanel simulacion;
    private JPanel izquierda;
    private JButton btnIniciar;
    private JButton btnFinalizar;
    private JPanel sim;
    private JPanel panel_2;
    private JLabel lblCantSol;
    private JTextField cantSol;
    private JPanel panel_3;
    private JLabel lblEstadoAmbulancia;
    private JTextArea textAreaEstadoAmbulancia;
    private JLabel lblCantAsociados;
    private JTextField cantAso;
    private JScrollPane scrollPane_1;
    private JLabel lblN_M;
    private JTextField textFieldN_M;
    private JPanel panel_1;
    private JButton btnSolMan;
    private JPanel SolMan;

    public JframeSimulacion() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // --- tamaño inicial más chico y ventana redimensionable ---
        setResizable(true);
        // NO usamos setBounds fijo enorme
        // setBounds(100, 100, 1201, 220);

        this.contentPane = new JPanel();
        this.contentPane.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

        // CAMBIO: BorderLayout en vez de GridLayout(0,2)
        this.setContentPane(this.contentPane);
        this.contentPane.setLayout(new BorderLayout(5, 5));

        this.Principal = new JPanel();
        this.Principal.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.contentPane.add(this.Principal, BorderLayout.CENTER);
        this.Principal.setLayout(new GridLayout(1, 1, 0, 0));  // un solo panel grande a la izquierda

        this.panel = new JPanel();
        this.panel.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.Principal.add(this.panel);

        // CAMBIO: GridBagLayout sin columnWidths/rowHeights gigantes
        GridBagLayout gbl_panel = new GridBagLayout();
        gbl_panel.columnWeights = new double[]{1.0};
        gbl_panel.rowWeights = new double[]{0.0, 0.0, 1.0, 0.0, 1.0};
        this.panel.setLayout(gbl_panel);

        this.izquierda = new JPanel();
        this.izquierda.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        GridBagConstraints gbc_izquierda = new GridBagConstraints();
        gbc_izquierda.gridheight = 3;
        gbc_izquierda.fill = GridBagConstraints.BOTH;
        gbc_izquierda.insets = new Insets(0, 0, 5, 0);
        gbc_izquierda.gridx = 0;
        gbc_izquierda.gridy = 0;
        this.panel.add(this.izquierda, gbc_izquierda);
        this.izquierda.setLayout(new GridLayout(0, 1, 0, 0));

        this.operario = new JPanel();
        this.operario.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.izquierda.add(this.operario);
        this.operario.setBorder(new TitledBorder(null, "Operario", TitledBorder.LEADING, TitledBorder.TOP, null, null));
        this.operario.setLayout(new GridLayout(2, 0, 0, 0));

        this.panel_1 = new JPanel();
        this.operario.add(this.panel_1);

        this.lblN_M = new JLabel("Nombre y apellido");
        this.panel_1.add(this.lblN_M);

        this.textFieldN_M = new JTextField();
        this.panel_1.add(this.textFieldN_M);
        this.textFieldN_M.setColumns(10);

        this.SolMan = new JPanel();
        this.operario.add(this.SolMan);

        this.btnSolMan = new JButton("Solicitar mantenimiento");
        this.SolMan.add(this.btnSolMan);

        this.estadoAmbulancia = new JPanel();
        this.estadoAmbulancia.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.izquierda.add(this.estadoAmbulancia);
        this.estadoAmbulancia.setBorder(new TitledBorder(null, "Ambulancia", TitledBorder.LEADING, TitledBorder.TOP, null, null));
        this.estadoAmbulancia.setLayout(new GridLayout(0, 1, 0, 0));

        this.panel_3 = new JPanel();
        FlowLayout flowLayout = (FlowLayout) this.panel_3.getLayout();
        flowLayout.setAlignment(FlowLayout.LEFT);
        this.estadoAmbulancia.add(this.panel_3);

        this.lblEstadoAmbulancia = new JLabel("Estado de la ambulancia:");
        this.lblEstadoAmbulancia.setFont(new Font("Segoe UI", Font.PLAIN, 14));  // un poco más chico
        this.lblEstadoAmbulancia.setVerticalAlignment(SwingConstants.BOTTOM);
        this.lblEstadoAmbulancia.setHorizontalAlignment(SwingConstants.LEFT);
        this.panel_3.add(this.lblEstadoAmbulancia);

        // Tamaño preferido más chico: 2 filas, 15 columnas
        this.textAreaEstadoAmbulancia = new JTextArea(2, 15);
        this.textAreaEstadoAmbulancia.setEditable(false);
        this.panel_3.add(this.textAreaEstadoAmbulancia);

        this.simulacion = new JPanel();
        this.simulacion.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.simulacion.setBorder(new TitledBorder(null, "Simulacion", TitledBorder.LEADING, TitledBorder.TOP, null, null));
        GridBagConstraints gbc_simulacion = new GridBagConstraints();
        gbc_simulacion.gridheight = 2;
        gbc_simulacion.insets = new Insets(0, 0, 5, 0);
        gbc_simulacion.fill = GridBagConstraints.BOTH;
        gbc_simulacion.gridx = 0;
        gbc_simulacion.gridy = 3;
        this.panel.add(this.simulacion, gbc_simulacion);

        // CAMBIO: BorderLayout para que el panel de botones no ensanche tanto
        this.simulacion.setLayout(new BorderLayout());

        this.sim = new JPanel();
        this.simulacion.add(this.sim, BorderLayout.CENTER);

        this.lblCantSol = new JLabel("Cantidad de solicitudes");
        this.sim.add(this.lblCantSol);

        this.cantSol = new JTextField();
        this.sim.add(this.cantSol);
        this.cantSol.setColumns(5);

        this.lblCantAsociados = new JLabel("Cantidad de asociados");
        this.sim.add(this.lblCantAsociados);

        this.cantAso = new JTextField();
        this.sim.add(this.cantAso);
        this.cantAso.setColumns(5);

        this.panel_2 = new JPanel();
        this.simulacion.add(this.panel_2, BorderLayout.EAST);

        this.btnIniciar = new JButton("Iniciar");
        this.panel_2.add(this.btnIniciar);

        this.btnFinalizar = new JButton("Finalizar");
        this.panel_2.add(this.btnFinalizar);

        this.movimientosAsociado = new JPanel();
        this.movimientosAsociado.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.movimientosAsociado.setBorder(new TitledBorder(null, "Notificaciones del Asociado", TitledBorder.LEADING, TitledBorder.TOP, null, null));

        // CAMBIO: la pongo a la derecha con tamaño preferido
        this.movimientosAsociado.setPreferredSize(new java.awt.Dimension(350, 200));
        this.contentPane.add(this.movimientosAsociado, BorderLayout.EAST);

        this.movimientosAsociado.setLayout(new GridLayout(1, 1, 0, 0));
        this.scrollPane_1 = new JScrollPane();
        this.movimientosAsociado.add(this.scrollPane_1);

        // textarea más chico (5 filas, 25 columnas)
        this.txtAsociado = new JTextArea(5, 25);
        this.txtAsociado.setEditable(false);
        this.scrollPane_1.setViewportView(this.txtAsociado);
        this.txtAsociado.setFont(new Font("Segoe UI", Font.PLAIN, 13));

        // --- muy importante: dejar que Swing calcule tamaño y arrancar más chico ---
        pack();                         // calcula tamaño mínimo según contenido
        setSize(900, 400);              // tamaño inicial razonable
        setLocationRelativeTo(null);    // centrar la ventana
    }

    public JTextField getCantSolicitudes() {
        return this.cantSol;
    }

    public void setEstadoAmbulancia(String estado) {
        this.textAreaEstadoAmbulancia.setText(estado);
        assert estado != null : "no puede tener un string nulo";
    }

    public void addAccionAmbulancia(String accion) {
        this.txtAsociado.append(accion + "\n");
    }

    public void arranca() {
        this.setVisible(true);
    }

    public void cerrar() {
        this.dispose();
    }

    public void appendMovimientosAsociados(String mensaje) {
        this.txtAsociado.append(mensaje + "\n");
    }

    public JTextField getNombreyApellido() {
        return this.textFieldN_M;
    }

    public JTextField getCantAsociados() {
        return this.cantAso;
    }

    @Override
    public void addActionListener(ActionListener l) {
        this.btnIniciar.addActionListener(l);
        this.btnFinalizar.addActionListener(l);
        this.btnSolMan.addActionListener(l);
    }

    public void keyPressed(KeyEvent e) { }

    public void keyReleased(KeyEvent e) {
        try {
            int h = Integer.parseInt(this.getCantSolicitudes().getText());
            this.btnIniciar.setEnabled(true);
        } catch (NumberFormatException exception) {
            this.btnIniciar.setEnabled(false);
        }
    }

    public void keyTyped(KeyEvent e) { }
}