package segundaEntrega.vista;

import segundaEntrega.modelo.negocio.Asociado;

import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.GridLayout;
import javax.swing.border.EtchedBorder;
import javax.swing.border.TitledBorder;
import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class JframeBD extends JFrame implements IVistaBD
{

    private static final long serialVersionUID = 1L;
    private JPanel panelPrincipal;
    private JPanel panel;
    private JPanel panelDatosAsociado;
    private JPanel nombre;
    private JLabel lblNombre;
    private JPanel nombre2;
    private JTextField textFieldNombre;
    private JPanel apellido;
    private JLabel lblApellido;
    private JPanel apellido2;
    private JTextField textFieldApellido;
    private JPanel dni;
    private JLabel lblDNI;
    private JPanel dni2;
    private JTextField textFieldDNI;
    private JPanel telefono;
    private JLabel lblTelefono;
    private JPanel telefono2;
    private JTextField textFieldTelefono;
    private JPanel ciudad;
    private JLabel lblCiudad;
    private JPanel ciudad2;
    private JTextField textFieldCiudad;
    private JPanel calle;
    private JLabel lblCalle;
    private JPanel calle2;
    private JTextField textFieldCalle;
    private JPanel numero;
    private JLabel lblNumero;
    private JPanel numero2;
    private JTextField textFieldNumero;
    private JPanel panelAB;
    private JButton btnAltaAsociados;
    private JButton btnBajaAsociados;
    private JPanel panelListado;
    private JList<Asociado> list;
    private JPanel altaAsociado;
    private JPanel bajaAsociado;
    private JPanel borrarDB;
    private JButton btnBorrarDB;
    private DefaultListModel<Asociado> modeloLista;
    private JPanel datoPrueba;
    private JButton btnAgregaDatosPrueba;



    /**
     * Create the frame.
     */
    public JframeBD() {
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setBounds(100, 100, 590, 504);
        this.panelPrincipal = new JPanel();
        this.panelPrincipal.setBorder(new EmptyBorder(5, 5, 5, 5));
        setContentPane(this.panelPrincipal);
        this.panelPrincipal.setLayout(new GridLayout(2, 1, 0, 0));

        this.panel = new JPanel();
        this.panelPrincipal.add(this.panel);
        this.panel.setLayout(new GridLayout(0, 2, 0, 0));

        this.panelDatosAsociado = new JPanel();
        this.panelDatosAsociado.setBorder(new TitledBorder(new EtchedBorder(EtchedBorder.LOWERED, new Color(255, 255, 255), new Color(160, 160, 160)), "Datos del Asociado", TitledBorder.LEFT, TitledBorder.ABOVE_TOP, null, new Color(0, 0, 0)));
        this.panel.add(this.panelDatosAsociado);
        this.panelDatosAsociado.setLayout(new GridLayout(0, 2, 0, 0));

        this.nombre = new JPanel();
        this.panelDatosAsociado.add(this.nombre);

        this.lblNombre = new JLabel("Nombre");
        this.lblNombre.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.nombre.add(this.lblNombre);

        this.nombre2 = new JPanel();
        this.panelDatosAsociado.add(this.nombre2);

        this.textFieldNombre = new JTextField();
        this.textFieldNombre.setFont(new Font("Tahoma", Font.PLAIN, 10));
        this.textFieldNombre.setColumns(10);
        this.nombre2.add(this.textFieldNombre);

        this.apellido = new JPanel();
        this.panelDatosAsociado.add(this.apellido);

        this.lblApellido = new JLabel("Apellido");
        this.lblApellido.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.apellido.add(this.lblApellido);

        this.apellido2 = new JPanel();
        this.panelDatosAsociado.add(this.apellido2);

        this.textFieldApellido = new JTextField();
        this.textFieldApellido.setColumns(10);
        this.apellido2.add(this.textFieldApellido);

        this.dni = new JPanel();
        this.panelDatosAsociado.add(this.dni);

        this.lblDNI = new JLabel("DNI");
        this.lblDNI.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.dni.add(this.lblDNI);

        this.dni2 = new JPanel();
        this.panelDatosAsociado.add(this.dni2);

        this.textFieldDNI = new JTextField();
        this.textFieldDNI.setColumns(10);
        this.dni2.add(this.textFieldDNI);

        this.telefono = new JPanel();
        this.panelDatosAsociado.add(this.telefono);

        this.lblTelefono = new JLabel("Telefono");
        this.lblTelefono.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.telefono.add(this.lblTelefono);

        this.telefono2 = new JPanel();
        this.panelDatosAsociado.add(this.telefono2);

        this.textFieldTelefono = new JTextField();
        this.textFieldTelefono.setColumns(10);
        this.telefono2.add(this.textFieldTelefono);

        this.ciudad = new JPanel();
        this.panelDatosAsociado.add(this.ciudad);

        this.lblCiudad = new JLabel("Ciudad");
        this.lblCiudad.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.ciudad.add(this.lblCiudad);

        this.ciudad2 = new JPanel();
        this.panelDatosAsociado.add(this.ciudad2);

        this.textFieldCiudad = new JTextField();
        this.textFieldCiudad.setColumns(10);
        this.ciudad2.add(this.textFieldCiudad);

        this.calle = new JPanel();
        this.panelDatosAsociado.add(this.calle);

        this.lblCalle = new JLabel("Calle");
        this.lblCalle.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.calle.add(this.lblCalle);

        this.calle2 = new JPanel();
        this.panelDatosAsociado.add(this.calle2);

        this.textFieldCalle = new JTextField();
        this.textFieldCalle.setColumns(10);
        this.calle2.add(this.textFieldCalle);

        this.numero = new JPanel();
        this.panelDatosAsociado.add(this.numero);

        this.lblNumero = new JLabel("Numero");
        this.lblNumero.setFont(new Font("Segoe UI", Font.PLAIN, 13));
        this.numero.add(this.lblNumero);

        this.numero2 = new JPanel();
        this.panelDatosAsociado.add(this.numero2);

        this.textFieldNumero = new JTextField();
        this.textFieldNumero.setColumns(10);
        this.numero2.add(this.textFieldNumero);

        this.panelAB = new JPanel();
        this.panelAB.setBorder(new TitledBorder(new EtchedBorder(EtchedBorder.LOWERED, new Color(255, 255, 255), new Color(160, 160, 160)), "Altas y Bajas", TitledBorder.CENTER, TitledBorder.ABOVE_TOP, null, new Color(0, 0, 0)));
        this.panel.add(this.panelAB);
        this.panelAB.setLayout(new GridLayout(0, 1, 0, 0));

        this.altaAsociado = new JPanel();
        this.panelAB.add(this.altaAsociado);

        this.btnAltaAsociados = new JButton("Alta Asociado");
        this.altaAsociado.add(this.btnAltaAsociados);
        this.btnAltaAsociados.setFont(new Font("Segoe UI Semibold", Font.BOLD, 20));

        this.bajaAsociado = new JPanel();
        this.panelAB.add(this.bajaAsociado);

        this.btnBajaAsociados = new JButton("Baja Asociado");
        this.bajaAsociado.add(this.btnBajaAsociados);
        this.btnBajaAsociados.setFont(new Font("Segoe UI Semibold", Font.BOLD, 20));
        this.btnBajaAsociados.setForeground(Color.BLACK);
        
        this.datoPrueba = new JPanel();
        this.panelAB.add(this.datoPrueba);
        
        this.btnAgregaDatosPrueba = new JButton("Agrega datos de prueba");
        this.btnAgregaDatosPrueba.setFont(new Font("Segoe UI Semibold", Font.PLAIN, 20));
        this.datoPrueba.add(this.btnAgregaDatosPrueba);

        this.borrarDB = new JPanel();
        this.panelAB.add(this.borrarDB);

        this.btnBorrarDB = new JButton("Borrar DB");
        this.btnBorrarDB.setForeground(Color.BLACK);
        this.btnBorrarDB.setFont(new Font("Segoe UI Semibold", Font.BOLD, 20));
        this.borrarDB.add(this.btnBorrarDB);

        this.panelListado = new JPanel();
        this.panelListado.setBorder(new TitledBorder(new EtchedBorder(EtchedBorder.LOWERED, new Color(255, 255, 255), new Color(160, 160, 160)), "Lista Asociados", TitledBorder.LEFT, TitledBorder.ABOVE_TOP, null, new Color(0, 0, 0)));
        this.panelPrincipal.add(this.panelListado);
        this.panelListado.setLayout(new GridLayout(0, 1, 0, 0));

        this.list = new JList<Asociado>();
        this.panelListado.add(this.list);

        this.modeloLista=new DefaultListModel<Asociado>();
        this.list.setModel(this.modeloLista);
        this.panelListado.add(new JScrollPane(list));

    }
    @Override
    public void addActionListener(ActionListener l) {
        this.btnAltaAsociados.addActionListener(l);
        this.btnBajaAsociados.addActionListener(l);
        this.btnBorrarDB.addActionListener(l);
    }
    @Override
    public void arranca(){
        this.setVisible(true);
    }
    @Override
    public void cerrar()
    {
        this.dispose();
    }
    @Override
    public JTextField getNombre(){
        return this.textFieldCalle;
    }
    @Override
    public JTextField getApellido()
    {
        return this.textFieldCalle;
    }
    @Override
    public JTextField getCiudad()
    {
        return this.textFieldCalle;
    }
    @Override
    public JTextField getDNI()
    {
        return this.textFieldCalle;
    }
    @Override
    public JTextField getTelefono()
    {
        return this.textFieldCalle;
    }
    @Override
    public JTextField getNumero()
    {
        return this.textFieldCalle;
    }
    @Override
    public JTextField getCalle()
    {
        return this.textFieldCalle;
    }

    public Asociado getAsociadoSeleccionado() { return (Asociado)this.list.getSelectedValue(); }

    public JButton getbtnAltaAsociados(){return this.btnAltaAsociados;}

    public JButton getbtnBajaAsociados(){return this.btnBajaAsociados;}

    public JButton getbtnBorrarDB(){return this.btnBorrarDB;}

    public JPanel getJPanel(){ return this.panelPrincipal;}

    @Override
    public void actualizaLista(ArrayList<Asociado> listaAsociados) {
        this.modeloLista.clear();
        for (Asociado a : listaAsociados) {
            this.modeloLista.addElement(a);
        }
        this.repaint();
    }
}
