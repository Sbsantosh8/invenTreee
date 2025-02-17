// // // // // import { useState, useEffect } from 'react';
// // // // // import { FiPlus, FiX } from "react-icons/fi"; // Plus for opening form, X for cancel
// // // // // import './Invoice.css';
 
// // // // // const Invoice = () => {
// // // // //   const [quotationId, setQuotationId] = useState('');
// // // // //   const [leadId, setLeadId] = useState('');
// // // // //   const [paidAmount, setPaidAmount] = useState('');
// // // // //   const [dueDate, setDueDate] = useState('');
// // // // //   const [responseMessage, setResponseMessage] = useState('');
// // // // //   const [loading, setLoading] = useState(false);
// // // // //   const [showForm, setShowForm] = useState(false);
 
// // // // //   interface Invoice {
// // // // //     id: number;
// // // // //     quotation: number;
// // // // //     quotation_number: string;
// // // // //     invoice_number: string;
// // // // //     total_amount: string;
// // // // //     paid_amount: string;
// // // // //     amount_due: string;
// // // // //     status: string;
// // // // //     created_at: string;
// // // // //     lead_id?: number;
// // // // //     due_date?: string;
// // // // //   }
 
 
 
// // // // //   interface Quotation {
// // // // //     id: number;
// // // // //     name: string;
// // // // //     lead: number;
// // // // //   }
 
// // // // //   interface Lead {
// // // // //     id: number;
// // // // //     lead_number: string;
// // // // //     name: string;
// // // // //     email: string;
// // // // //     phone: string;
// // // // //     address: string;
// // // // //     source: string;
// // // // //     status: string;
// // // // //     notes: string | null;
// // // // //     created_at: string;
// // // // //     updated_at: string;
// // // // //   }
 
// // // // //   const [invoices, setInvoices] = useState<Invoice[]>([]);
// // // // //   const [quotations, setQuotations] = useState<Quotation[]>([]);
// // // // //   const [leads, setLeads] = useState<Lead[]>([]); // Use appropriate type for leads
 
 
// // // // //   useEffect(() => {
// // // // //     document.title = 'Invoice';
// // // // //     fetchInvoices();
// // // // //     fetchQuotations();
// // // // //     fetchLeads();
// // // // //   }, []);
 
// // // // //   const fetchInvoices = async () => {
// // // // //     try {
// // // // //       setLoading(true);
// // // // //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/');
// // // // //       const result = await response.json();
// // // // //       if (response.ok) {
// // // // //         setInvoices(result);
// // // // //       } else {
// // // // //         setResponseMessage(result.error || 'An error occurred.');
// // // // //       }
// // // // //     } catch (error) {
// // // // //       console.error('Error fetching invoices:', error);
// // // // //       setResponseMessage('An error occurred while fetching the invoices.');
// // // // //     } finally {
// // // // //       setLoading(false);
// // // // //     }
// // // // //   };
 
// // // // //   const fetchLeads = async () => {
// // // // //     try {
// // // // //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/leads/'); // Adjust API endpoint if necessary
// // // // //       const result = await response.json();
// // // // //       if (response.ok) {
// // // // //         setLeads(result);
// // // // //       } else {
// // // // //         console.error('Failed to fetch leads:', result.error);
// // // // //       }
// // // // //     } catch (error) {
// // // // //       console.error('Error fetching leads:', error);
// // // // //     }
// // // // //   };
 
// // // // //   const fetchQuotations = async () => {
// // // // //     try {
// // // // //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/quotations/');
// // // // //       const result = await response.json();
// // // // //       if (response.ok) {
// // // // //         setQuotations(result);
// // // // //       } else {
// // // // //         console.error('Failed to fetch quotations:', result.error);
// // // // //       }
// // // // //     } catch (error) {
// // // // //       console.error('Error fetching quotations:', error);
// // // // //     }
// // // // //   };
 
// // // // //   const getLeadNameById = (leadId: number | string) => {
// // // // //     const lead = leads.find((lead) => lead.id === Number(leadId));
// // // // //     return lead ? lead.name : 'N/A'; // Return 'N/A' if the lead is not found
// // // // //   };
 
// // // // //   const getStatusDisplay = (status: string) => {
// // // // //     switch (status) {
// // // // //       case 'partially_paid':
// // // // //         return 'Partially Paid';
// // // // //       case 'paid':
// // // // //         return 'Paid';
// // // // //       case 'unpaid':
// // // // //         return 'Unpaid';
// // // // //       default:
// // // // //         return status;
// // // // //     }
 
// // // // //   };
 
 
 
 
// // // // //   const handleQuotationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
// // // // //     const selectedQuotationId = e.target.value;
// // // // //     setQuotationId(selectedQuotationId);
// // // // //     const selectedQuotation = quotations.find((q) => q.id === Number(selectedQuotationId));
// // // // //     setLeadId(selectedQuotation ? String(selectedQuotation.lead) : '');
// // // // //   };
 
// // // // //   const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
// // // // //     e.preventDefault();
// // // // //     const data = {
// // // // //       quotation_id: quotationId,
// // // // //       lead_id: leadId,
// // // // //       paid_amount: paidAmount,
// // // // //       due_date: dueDate,
// // // // //     };
 
// // // // //     try {
// // // // //       setLoading(true);
// // // // //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
// // // // //         method: 'POST',
// // // // //         headers: {
// // // // //           'Content-Type': 'application/json',
// // // // //         },
// // // // //         body: JSON.stringify(data),
// // // // //       });
 
// // // // //       const result = await response.json();
// // // // //       if (response.ok) {
// // // // //         setResponseMessage(result.message || 'Invoice created successfully!');
// // // // //         fetchInvoices();
// // // // //         setShowForm(false); // Close form after submission
// // // // //       } else {
// // // // //         setResponseMessage(result.error || 'An error occurred.');
// // // // //       }
// // // // //     } catch (error) {
// // // // //       console.error('Error creating invoice:', error);
// // // // //       setResponseMessage('An error occurred while creating the invoice.');
// // // // //     } finally {
// // // // //       setLoading(false);
// // // // //     }
// // // // //   };
 
// // // // //   return (
// // // // //     <div>
// // // // //       <h2>Invoices</h2>
// // // // //       <button type="button" className="open-form-button" onClick={() => setShowForm(true)}>
// // // // //         <FiPlus /> Create Invoice
// // // // //       </button>
 
// // // // //       {responseMessage && <p>{responseMessage}</p>}
 
// // // // //       {showForm && (
// // // // //         <div className="invoice-form-overlay">
// // // // //           <div className="invoice-form-container">
// // // // //             <button type="button" className="close-form-button" onClick={() => setShowForm(false)}>
// // // // //               <FiX />
// // // // //             </button>
// // // // //             <h2>Create Invoice</h2>
// // // // //             <form onSubmit={handleSubmit}>
// // // // //               <div>
// // // // //                 <label>
// // // // //                   Quotation Id:
// // // // //                   <select value={quotationId} onChange={handleQuotationChange} required>
// // // // //                     <option value="">Select a Quotation</option>
// // // // //                     {quotations.map((quotation) => (
// // // // //                       <option key={quotation.id} value={quotation.id}>
// // // // //                         {quotation.name || `${quotation.id}`}
// // // // //                       </option>
// // // // //                     ))}
// // // // //                   </select>
// // // // //                 </label>
// // // // //               </div>
// // // // //               <div>
// // // // //                 <label>
// // // // //                   Lead ID:
// // // // //                   <input type="number" value={leadId} readOnly required />
// // // // //                 </label>
// // // // //               </div>
// // // // //               <div>
// // // // //                 <label>
// // // // //                   Paid Amount:
// // // // //                   <input
// // // // //                     type="number"
// // // // //                     value={paidAmount}
// // // // //                     onChange={(e) => setPaidAmount(e.target.value)}
// // // // //                     required
// // // // //                   />
// // // // //                 </label>
// // // // //               </div>
// // // // //               <div>
// // // // //                 <label>
// // // // //                   Due Date:
// // // // //                   <input
// // // // //                     type="datetime-local"
// // // // //                     value={dueDate}
// // // // //                     onChange={(e) => setDueDate(e.target.value)}
// // // // //                     required
// // // // //                   />
// // // // //                 </label>
// // // // //               </div>
// // // // //               <button type="submit" disabled={loading}>
// // // // //                 {loading ? 'Submitting...' : 'Create Invoice'}
// // // // //               </button>
// // // // //             </form>
// // // // //           </div>
// // // // //         </div>
// // // // //       )}
 
// // // // // {loading ? (
// // // // //   <p>Loading...</p>
// // // // // ) : (
// // // // //   <>
// // // // //     <h2>Invoices List</h2>
// // // // //     <table
// // // // //       className="invoice-table"
// // // // //       style={{
// // // // //         borderCollapse: 'separate',  // Ensure separate borders for the cells
// // // // //         borderSpacing: '0',
// // // // //         borderRadius: '10px',        // Rounded corners
// // // // //         overflow: 'hidden',          // Ensure rounding works
// // // // //         backgroundColor: 'white',    // Background color
// // // // //         border: '1px solid black',   // Black border for the table
// // // // //       }}
// // // // //     >
// // // // //       <thead style={{ border: 'none' }}>
// // // // //         <tr>
// // // // //           {/* <th>Invoice ID</th>
// // // // //           <th>Quotation ID</th> */}
// // // // //           <th>Quotation Number</th>
// // // // //           <th>Invoice Number</th>
// // // // //           <th>Total Amount</th>
// // // // //           <th>Paid Amount</th>
// // // // //           <th>Amount Due</th>
// // // // //           <th>Status</th>
// // // // //           <th>Created Date</th>
// // // // //           <th>Lead</th>
// // // // //           <th>Due Date</th>
// // // // //         </tr>
// // // // //       </thead>
// // // // //       <tbody>
// // // // //         {invoices.map((invoice) => (
 
         
// // // // //           <tr key={invoice.id}>
// // // // //             {/* <td>{invoice.id}</td>
// // // // //             <td>{invoice.quotation}</td> */}
// // // // //             <td>{invoice.quotation_number}</td>
// // // // //             <td>{invoice.invoice_number}</td>
// // // // //             <td>{invoice.total_amount}</td>
// // // // //             <td>{invoice.paid_amount}</td>
// // // // //             <td>{invoice.amount_due}</td>
// // // // //             {/* <td>{invoice.status}</td> */}
// // // // //             <td>{getStatusDisplay(invoice.status)}</td>
// // // // //             <td>{invoice.created_at}</td>
           
// // // // //             {/* <td>{invoice.lead_id ?? 'N/A'}</td> */}
// // // // //             <td>{getLeadNameById(invoice.lead_id ?? '')}</td>
// // // // //             <td>{invoice.due_date ?? 'N/A'}</td>
// // // // //           </tr>
// // // // //         ))}
// // // // //       </tbody>
// // // // //     </table>
// // // // //   </>
// // // // // )}
// // // // //     </div>
// // // // //   );
// // // // // };
 
// // // // // export default  Invoice ;





// // // // import { useState, useEffect } from 'react';
// // // // import { FiX } from "react-icons/fi"; // X for cancel
// // // // import './Invoice.css';

// // // // const Invoice = ({ onClose }: { onClose: () => void }) => {
// // // //   const [quotationId, setQuotationId] = useState('');
// // // //   const [leadId, setLeadId] = useState('');
// // // //   const [paidAmount, setPaidAmount] = useState('');
// // // //   const [dueDate, setDueDate] = useState('');
// // // //   const [responseMessage, setResponseMessage] = useState('');
// // // //   const [loading, setLoading] = useState(false);

// // // //   interface Quotation {
// // // //     id: number;
// // // //     name: string;
// // // //     lead: number;
// // // //   }

// // // //   const [quotations, setQuotations] = useState<Quotation[]>([]);

// // // //   useEffect(() => {
// // // //     document.title = 'Invoice';
// // // //     fetchQuotations();
// // // //   }, []);

// // // //   const fetchQuotations = async () => {
// // // //     try {
// // // //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/quotations/');
// // // //       const result = await response.json();
// // // //       if (response.ok) {
// // // //         setQuotations(result);
// // // //       } else {
// // // //         console.error('Failed to fetch quotations:', result.error);
// // // //       }
// // // //     } catch (error) {
// // // //       console.error('Error fetching quotations:', error);
// // // //     }
// // // //   };

// // // //   const handleQuotationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
// // // //     const selectedQuotationId = e.target.value;
// // // //     setQuotationId(selectedQuotationId);
// // // //     const selectedQuotation = quotations.find((q) => q.id === Number(selectedQuotationId));
// // // //     setLeadId(selectedQuotation ? String(selectedQuotation.lead) : '');
// // // //   };

// // // //   const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
// // // //     e.preventDefault();
// // // //     const data = {
// // // //       quotation_id: quotationId,
// // // //       lead_id: leadId,
// // // //       paid_amount: paidAmount,
// // // //       due_date: dueDate,
// // // //     };

// // // //     try {
// // // //       setLoading(true);
// // // //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
// // // //         method: 'POST',
// // // //         headers: {
// // // //           'Content-Type': 'application/json',
// // // //         },
// // // //         body: JSON.stringify(data),
// // // //       });

// // // //       const result = await response.json();
// // // //       if (response.ok) {
// // // //         setResponseMessage(result.message || 'Invoice created successfully!');
// // // //         setShowForm(false); // Close form after submission
// // // //         onClose(); // Close the form
// // // //       } else {
// // // //         setResponseMessage(result.error || 'An error occurred.');
// // // //       }
// // // //     } catch (error) {
// // // //       console.error('Error creating invoice:', error);
// // // //       setResponseMessage('An error occurred while creating the invoice.');
// // // //     } finally {
// // // //       setLoading(false);
// // // //     }
// // // //   };

// // // //   return (
// // // //     <div>
// // // //       <button type="button" className="close-form-button" onClick={onClose}>
// // // //         <FiX />
// // // //       </button>
// // // //       <h2>Create Invoice</h2>
// // // //       <form onSubmit={handleSubmit}>
// // // //         <div>
// // // //           <label>
// // // //             Quotation Id:
// // // //             <select value={quotationId} onChange={handleQuotationChange} required>
// // // //               <option value="">Select a Quotation</option>
// // // //               {quotations.map((quotation) => (
// // // //                 <option key={quotation.id} value={quotation.id}>
// // // //                   {quotation.name || `${quotation.id}`}
// // // //                 </option>
// // // //               ))}
// // // //             </select>
// // // //           </label>
// // // //         </div>
// // // //         <div>
// // // //           <label>
// // // //             Lead ID:
// // // //             <input type="number" value={leadId} readOnly required />
// // // //           </label>
// // // //         </div>
// // // //         <div>
// // // //           <label>
// // // //             Paid Amount:
// // // //             <input
// // // //               type="number"
// // // //               value={paidAmount}
// // // //               onChange={(e) => setPaidAmount(e.target.value)}
// // // //               required
// // // //             />
// // // //           </label>
// // // //         </div>
// // // //         <div>
// // // //           <label>
// // // //             Due Date:
// // // //             <input
// // // //               type="datetime-local"
// // // //               value={dueDate}
// // // //               onChange={(e) => setDueDate(e.target.value)}
// // // //               required
// // // //             />
// // // //           </label>
// // // //         </div>
// // // //         <button type="submit" disabled={loading}>
// // // //           {loading ? 'Submitting...' : 'Create Invoice'}
// // // //         </button>
// // // //       </form>
// // // //       {responseMessage && <p>{responseMessage}</p>}
// // // //     </div>
// // // //   );
// // // // };

// // // // export default Invoice;


// // // import { useState, useEffect } from 'react';
// // // import { FiX } from "react-icons/fi"; // X for cancel
// // // import './Invoice.css';

// // // const Invoice = ({ onClose }: { onClose: () => void }) => {
// // //   const [quotationId, setQuotationId] = useState('');
// // //   const [leadId, setLeadId] = useState('');
// // //   const [paidAmount, setPaidAmount] = useState('');
// // //   const [dueDate, setDueDate] = useState('');
// // //   const [responseMessage, setResponseMessage] = useState('');
// // //   const [loading, setLoading] = useState(false);

// // //   interface Quotation {
// // //     id: number;
// // //     name: string;
// // //     lead: number;
// // //   }

// // //   const [quotations, setQuotations] = useState<Quotation[]>([]);

// // //   useEffect(() => {
// // //     document.title = 'Invoice';
// // //     fetchQuotations();
// // //   }, []);

// // //   const fetchQuotations = async () => {
// // //     try {
// // //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/quotations/');
// // //       const result = await response.json();
// // //       if (response.ok) {
// // //         setQuotations(result);
// // //       } else {
// // //         console.error('Failed to fetch quotations:', result.error);
// // //       }
// // //     } catch (error) {
// // //       console.error('Error fetching quotations:', error);
// // //     }
// // //   };

// // //   const handleQuotationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
// // //     const selectedQuotationId = e.target.value;
// // //     setQuotationId(selectedQuotationId);
// // //     const selectedQuotation = quotations.find((q) => q.id === Number(selectedQuotationId));
// // //     setLeadId(selectedQuotation ? String(selectedQuotation.lead) : '');
// // //   };

// // //   const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
// // //     e.preventDefault();
// // //     const data = {
// // //       quotation_id: quotationId,
// // //       lead_id: leadId,
// // //       paid_amount: paidAmount,
// // //       due_date: dueDate,
// // //     };

// // //     try {
// // //       setLoading(true);
// // //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
// // //         method: 'POST',
// // //         headers: {
// // //           'Content-Type': 'application/json',
// // //         },
// // //         body: JSON.stringify(data),
// // //       });

// // //       const result = await response.json();
// // //       if (response.ok) {
// // //         setResponseMessage(result.message || 'Invoice created successfully!');
// // //         onClose(); // Close the form
// // //       } else {
// // //         console.error('Error response from server:', result.error);
// // //         setResponseMessage(result.error || 'An error occurred.');
// // //       }
// // //     } catch (error) {
// // //       console.error('Error creating invoice:', error);
// // //       setResponseMessage('An error occurred while creating the invoice.');
// // //     } finally {
// // //       setLoading(false);
// // //     }
// // //   };

// // //   return (
// // //     <div>
// // //       <button type="button" className="close-form-button" onClick={onClose}>
// // //         <FiX />
// // //       </button>
// // //       <h2>Create Invoice</h2>
// // //       <form onSubmit={handleSubmit}>
// // //         <div>
// // //           <label>
// // //             Quotation Id:
// // //             <select value={quotationId} onChange={handleQuotationChange} required>
// // //               <option value="">Select a Quotation</option>
// // //               {quotations.map((quotation) => (
// // //                 <option key={quotation.id} value={quotation.id}>
// // //                   {quotation.name || `${quotation.id}`}
// // //                 </option>
// // //               ))}
// // //             </select>
// // //           </label>
// // //         </div>
// // //         <div>
// // //           <label>
// // //             Lead ID:
// // //             <input type="number" value={leadId} readOnly required />
// // //           </label>
// // //         </div>
// // //         <div>
// // //           <label>
// // //             Paid Amount:
// // //             <input
// // //               type="number"
// // //               value={paidAmount}
// // //               onChange={(e) => setPaidAmount(e.target.value)}
// // //               required
// // //             />
// // //           </label>
// // //         </div>
// // //         <div>
// // //           <label>
// // //             Due Date:
// // //             <input
// // //               type="datetime-local"
// // //               value={dueDate}
// // //               onChange={(e) => setDueDate(e.target.value)}
// // //               required
// // //             />
// // //           </label>
// // //         </div>
// // //         <button type="submit" disabled={loading}>
// // //           {loading ? 'Submitting...' : 'Create Invoice'}
// // //         </button>
// // //       </form>
// // //       {responseMessage && <p>{responseMessage}</p>}
// // //     </div>
// // //   );
// // // };

// // // export default Invoice;




// // import { useState, useEffect } from 'react';
// // import { FiX } from "react-icons/fi"; // X for cancel
// // import { t } from '@lingui/macro';
// // import './Invoice.css'; // Import the CSS file
 
// // const Invoice = ({ onClose }: { onClose: () => void }) => {
// //   const [quotationId, setQuotationId] = useState('');
// //   const [leadId, setLeadId] = useState('');
// //   const [paidAmount, setPaidAmount] = useState('');
// //   const [dueDate, setDueDate] = useState('');
// //   const [responseMessage, setResponseMessage] = useState('');
// //   const [loading, setLoading] = useState(false);
 
// //   interface Quotation {
// //     id: number;
// //     name: string;
// //     lead: number;
// //   }
 
// //   const [quotations, setQuotations] = useState<Quotation[]>([]);
 
// //   useEffect(() => {
// //     document.title = 'Invoice';
// //     fetchQuotations();
// //   }, []);
 
// //   const fetchQuotations = async () => {
// //     try {
// //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/quotations/');
// //       const result = await response.json();
// //       if (response.ok) {
// //         setQuotations(result);
// //       } else {
// //         console.error('Failed to fetch quotations:', result.error);
// //       }
// //     } catch (error) {
// //       console.error('Error fetching quotations:', error);
// //     }
// //   };
 
// //   const handleQuotationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
// //     const selectedQuotationId = e.target.value;
// //     setQuotationId(selectedQuotationId);
// //     const selectedQuotation = quotations.find((q) => q.id === Number(selectedQuotationId));
// //     setLeadId(selectedQuotation ? String(selectedQuotation.lead) : '');
// //   };
 
// //   const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
// //     e.preventDefault();
// //     const data = {
// //       quotation_id: quotationId,
// //       lead_id: leadId,
// //       paid_amount: paidAmount,
// //       due_date: dueDate,
// //     };
 
// //     try {
// //       setLoading(true);
// //       const response = await fetch('http://127.0.0.1:8000/api/lead_to_invoice/invoices/', {
// //         method: 'POST',
// //         headers: {
// //           'Content-Type': 'application/json',
// //         },
// //         body: JSON.stringify(data),
// //       });
 
// //       const result = await response.json();
// //       if (response.ok) {
// //         setResponseMessage(result.message || 'Invoice created successfully!');
// //         onClose(); // Close the form after submission
// //       } else {
// //         setResponseMessage(result.error || 'An error occurred.');
// //       }
// //     } catch (error) {
// //       console.error('Error creating invoice:', error);
// //       // setResponseMessage('An error occurred while creating the invoice.');
// //       setResponseMessage('Please Enter Valid Data !');
// //     } finally {
// //       setLoading(false);
// //     }
// //   };
 
// //   return (
// //     <div className="invoice-form-overlay">
// //       <div className="invoice-form-container">
// //         <button type="button" className="close-form-button" onClick={onClose}>
// //           <FiX />
// //         </button>
// //         <h2>{t`Create Invoice`}</h2>
// //         <form onSubmit={handleSubmit}>
// //           <div className="form-group">
// //             <label>
// //               {t`Quotation Id`}:
// //               <select value={quotationId} onChange={handleQuotationChange} required>
// //                 <option value="">{t`Select a Quotation`}</option>
// //                 {quotations.map((quotation) => (
// //                   <option key={quotation.id} value={quotation.id}>
// //                     {quotation.name || `${quotation.id}`}
// //                   </option>
// //                 ))}
// //               </select>
// //             </label>
// //           </div>
// //           <div className="form-group">
// //             <label>
// //               {t`Lead ID`}:
// //               <input type="number" value={leadId} readOnly required />
// //             </label>
// //           </div>
// //           <div className="form-group">
// //             <label>
// //               {t`Paid Amount`}:
// //               <input
// //                 type="number"
// //                 value={paidAmount}
// //                 onChange={(e) => setPaidAmount(e.target.value)}
// //                 required
// //               />
// //             </label>
// //           </div>
// //           <div className="form-group">
// //             <label>
// //               {t`Due Date`}:
// //               <input
// //                 type="datetime-local"
// //                 value={dueDate}
// //                 onChange={(e) => setDueDate(e.target.value)}
// //                 required
// //               />
// //             </label>
// //           </div>
// //           <button type="submit" disabled={loading}>
// //             {loading ? t`Submitting...` : t`Create Invoice`}
// //           </button>
// //         </form>
// //         {responseMessage && <p>{responseMessage}</p>}
// //       </div>
// //     </div>
// //   );
// // };
 
// // export default Invoice;


// import { useState, useEffect } from 'react';
// import { FiX } from "react-icons/fi"; // X for cancel
// import { t } from '@lingui/macro';
// import './Invoice.css'; // Import the CSS file
 
// const Invoice = ({ onClose }: { onClose: () => void }) => {
//   const [quotationId, setQuotationId] = useState('');
//   const [quotationNumber, setQuotationNumber] = useState(''); 
//   const [leadId, setLeadId] = useState('');
//   const [paidAmount, setPaidAmount] = useState('');
//   const [dueDate, setDueDate] = useState('');
//   const [responseMessage, setResponseMessage] = useState('');
//   const [loading, setLoading] = useState(false);
 
//   interface Quotation {
//     id: number;
//     quotation_number:string;
//     name: string;
//     lead: number;
//   }
 
//   const [quotations, setQuotations] = useState<Quotation[]>([]);
 
//   useEffect(() => {
//     document.title = 'Invoice';
//     fetchQuotations();
//   }, []);
 
//   const fetchQuotations = async () => {
//     try {
//       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/quotations/');
//       const result = await response.json();
//       if (response.ok) {
//         setQuotations(result);
//        console.log(result);

//       } else {
//         console.error('Failed to fetch quotations:', result.error);
//       }
//     } catch (error) {
//       console.error('Error fetching quotations:', error);
//     }
//   };
 
//   // const handleQuotationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
//   //   const selectedQuotationId = e.target.value;
//   //   setQuotationId(selectedQuotationId);
//   //   const selectedQuotation = quotations.find((q) => q.id === Number(selectedQuotationId));
//   //   setLeadId(selectedQuotation ? String(selectedQuotation.lead) : '');
//   // };
//   const handleQuotationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
//     const selectedQuotationNumber = e.target.value;
//     setQuotationNumber(selectedQuotationNumber);
//     console.log(selectedQuotationNumber);
//     const selectedQuotation = quotations.find((q) => q.quotation_number === selectedQuotationNumber);
//     setQuotationId(selectedQuotation ? String(selectedQuotation.id) : '');
//     setLeadId(selectedQuotation ? String(selectedQuotation.lead) : '');
//   };


//   const handleDueDateChange = (e: React.ChangeEvent<HTMLInputElement>) => {
//     const date = e.target.value;
//     setDueDate(date);
//   };

//   const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
//     e.preventDefault();
  
   
//     const data = {
//       quotation_id: quotationId,
//       lead_id: leadId,
//       paid_amount: paidAmount,
//       due_date: dueDate,
//     };
 
//     try {
//       setLoading(true);
//       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data),
//       });
 
//       const result = await response.json();
//       if (response.ok) {
//         setResponseMessage(result.message || 'Invoice created successfully!');
//         onClose(); // Close the form after submission
//       } else {
//         setResponseMessage(result.error || 'An error occurred.');
//       }
//     } catch (error) {
//       console.error('Error creating invoice:', error);
//       setResponseMessage('Please Enter Valid Data !');    } finally {
//       setLoading(false);
//     }
//   };
 
//   return (
//     <div className="invoice-form-overlay">
//       <div className="invoice-form-container">
//         <button type="button" className="close-form-button" onClick={onClose}>
//           <FiX />
//         </button>
//         <h2>{t`Create Invoice`}</h2>
//         <form onSubmit={handleSubmit}>
//           <div className="form-group">
//             <label>
//               {t`Quotation Number`}:
//               <select value={quotationId} onChange={handleQuotationChange} required>
//                 <option value="">{t`Select a Quotation`}</option>
//                 {quotations.map((quotation) => (
//                   <option key={quotation.id} value={quotation.quotation_number}>
//                     {quotation.quotation_number}
//                   </option>
//                 ))}
//               </select>
//             </label>
//           </div>
//           <div className="form-group">
//             <label>
//               {t`Lead ID`}:
//               <input type="number" value={leadId} readOnly required />
//             </label>
//           </div>
//           <div className="form-group">
//             <label>
//               {t`Paid Amount`}:
//               <input
//                 type="number"
//                 value={paidAmount}
//                 onChange={(e) => setPaidAmount(e.target.value)}
//                 required
//               />
//             </label>
//           </div>
//           <div className="form-group">
//             <label>
//               {t`Due Date`}:
//               <input
//                 type="date"
                
//                 value={dueDate}
//                 onChange={ handleDueDateChange}
//                 required
//               />
//             </label>
//           </div>
//           <button type="submit" disabled={loading}>
//             {loading ? t`Submitting...` : t`Create Invoice`}
//           </button>
//         </form>
//         {responseMessage && <p>{responseMessage}</p>}
//       </div>
//     </div>
//   );
// };
 
// export default Invoice;




import { useState, useEffect } from 'react';
import { FiX } from "react-icons/fi"; // X for cancel
import { t } from '@lingui/macro';
import './Invoice.css'; // Import the CSS file

const Invoice = ({ onClose }: { onClose: () => void }) => {
  const [quotationId, setQuotationId] = useState('');
  const [quotationNumber, setQuotationNumber] = useState(''); // Add state for quotation number
  const [leadId, setLeadId] = useState('');
  const [paidAmount, setPaidAmount] = useState('');
  const [dueDate, setDueDate] = useState('');
  const [responseMessage, setResponseMessage] = useState('');
  const [loading, setLoading] = useState(false);

  interface Quotation {
    id: number;
    quotation_number: string;
    name: string;
    lead: number;
  }

  const [quotations, setQuotations] = useState<Quotation[]>([]);

  useEffect(() => {
    document.title = 'Invoice';
    fetchQuotations();
  }, []);

  const fetchQuotations = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/quotations/');
      const result = await response.json();
      if (response.ok) {
        setQuotations(result);
        console.log(result);
      } else {
        console.error('Failed to fetch quotations:', result.error);
      }
    } catch (error) {
      console.error('Error fetching quotations:', error);
    }
  };

  const handleQuotationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedQuotationNumber = e.target.value;
    setQuotationNumber(selectedQuotationNumber); // Update the quotation number state
    const selectedQuotation = quotations.find((q) => q.quotation_number === selectedQuotationNumber);
    setQuotationId(selectedQuotation ? String(selectedQuotation.id) : '');
    setLeadId(selectedQuotation ? String(selectedQuotation.lead) : '');
  };

  const handleDueDateChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const date = e.target.value;
    console.log("date",date);
    setDueDate(date);
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const [year, month, day] = dueDate.split('-');
    const formattedDueDate = `${day}-${month}-${year}`; // Format the due date to dd-mm-yyyy for backend

    const data = {
      quotation_id: quotationId,
      lead_id: leadId,
      paid_amount: paidAmount,
      due_date: formattedDueDate, // Send due_date in dd-mm-yyyy format
    };
console.log("formatted data",data.due_date);
    try {
      setLoading(true);
      const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      if (response.ok) {
        setResponseMessage(result.message || 'Invoice created successfully!');
        onClose(); // Close the form after submission
      } else {
        setResponseMessage(result.error || 'An error occurred.');
      }
    } catch (error) {
      console.error('Error creating invoice:', error);
      setResponseMessage('Please Enter Valid Data !');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="invoice-form-overlay">
      <div className="invoice-form-container">
        <button type="button" className="close-form-button" onClick={onClose}>
          <FiX />
        </button>
        <h2>{t`Create Invoice`}</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>
              {t`Quotation Number`}:
              <select value={quotationNumber} onChange={handleQuotationChange} required>
                <option value="">{t`Select a Quotation`}</option>
                {quotations.map((quotation) => (
                  <option key={quotation.id} value={quotation.quotation_number}>
                    {quotation.quotation_number}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <div className="form-group">
            <label>
              {t`Lead ID`}:
              <input type="number" value={leadId} readOnly required />
            </label>
          </div>
          <div className="form-group">
            <label>
              {t`Paid Amount`}:
              <input
                type="number"
                value={paidAmount}
                onChange={(e) => setPaidAmount(e.target.value)}
                required
              />
            </label>
          </div>
          <div className="form-group">
            <label>
              {t`Due Date`}:
              <input
                type="date"
                value={dueDate}
                onChange={handleDueDateChange}
                required
              />
            </label>
          </div>
          <button type="submit" disabled={loading}>
            {loading ? t`Submitting...` : t`Create Invoice`}
          </button>
        </form>
        {responseMessage && <p>{responseMessage}</p>}
      </div>
    </div>
  );
};

export default Invoice;