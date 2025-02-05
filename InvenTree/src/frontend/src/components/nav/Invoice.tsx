// // import type React from 'react';
// // import { useState, useEffect } from 'react';

// // const App = () => {
// //   const [quotationId, setQuotationId] = useState('');
// //   const [leadId, setLeadId] = useState('');
// //   const [paidAmount, setPaidAmount] = useState('');
// //   const [dueDate, setDueDate] = useState('');
// //   const [responseMessage, setResponseMessage] = useState('');
// //   const [loading, setLoading] = useState(false);

// //   interface Invoice {
// //     id: number;
// //     quotation: number;
// //     quotation_number: string;
// //     invoice_number: string;
// //     total_amount: string;
// //     paid_amount: string;
// //     amount_due: string;
// //     status: string;
// //     created_at: string;
// //     lead_id?: number;
// //     due_date?: string;
// //   }

// //   const [invoices, setInvoices] = useState<Invoice[]>([]);

// //   useEffect(() => {
// //     fetchInvoices();
// //   }, []);

// //   const fetchInvoices = async () => {
// //     try {
// //       setLoading(true); // Start loading

// //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
// //         method: 'GET',
// //         headers: {
// //           'Content-Type': 'application/json',
// //         },
// //       });

// //       const result = await response.json();
// //       console.log("result : ", result);

// //       if (response.ok) {
// //         setInvoices(result);
// //       } else {
// //         setResponseMessage(result.error || 'An error occurred.');
// //       }
// //     } catch (error) {
// //       console.error('Error fetching invoices:', error);
// //       setResponseMessage('An error occurred while fetching the invoices.');
// //     } finally {
// //       setLoading(false); // Stop loading
// //     }
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
// //       setLoading(true); // Start loading

// //       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
// //         method: 'POST',
// //         headers: {
// //           'Content-Type': 'application/json',
// //         },
// //         body: JSON.stringify(data),
// //       });

// //       const result = await response.json();
// //       console.log("result : ", result);

// //       if (response.ok) {
// //         setResponseMessage(result.message || 'Invoice created successfully!');
// //         setInvoices((prevInvoices) => [...prevInvoices, result.invoice]); // Add the new invoice to the list
// //       } else {
// //         setResponseMessage(result.error || 'An error occurred.');
// //       }
// //     } catch (error) {
// //       console.error('Error creating invoice:', error);
// //       setResponseMessage('An error occurred while creating the invoice.');
// //     } finally {
// //       setLoading(false); // Stop loading
// //     }
// //   };

// //   return (
// //     <div>
// //       <h2>Create Invoice</h2>
// //       <form onSubmit={handleSubmit}>
// //         <div>
// //           <label>
// //             Quotation ID:
// //             <input
// //               type="number"
// //               value={quotationId}
// //               onChange={(e) => setQuotationId(e.target.value)}
// //               required
// //             />
// //           </label>
// //         </div>
// //         <div>
// //           <label>
// //             Lead ID:
// //             <input
// //               type="number"
// //               value={leadId}
// //               onChange={(e) => setLeadId(e.target.value)}
// //               required
// //             />
// //           </label>
// //         </div>
// //         <div>
// //           <label>
// //             Paid Amount:
// //             <input
// //               type="number"
// //               value={paidAmount}
// //               onChange={(e) => setPaidAmount(e.target.value)}
// //               required
// //             />
// //           </label>
// //         </div>
// //         <div>
// //           <label>
// //             Due Date:
// //             <input
// //               type="datetime-local"
// //               value={dueDate}
// //               onChange={(e) => setDueDate(e.target.value)}
// //               required
// //             />
// //           </label>
// //         </div>
// //         <button type="submit" disabled={loading}>
// //           {loading ? 'Submitting...' : 'Create Invoice'}
// //         </button>
// //       </form>

// //       {responseMessage && <p>{responseMessage}</p>}

// //       <h2>Invoices</h2>
// //       {loading ? (
// //         <p>Loading...</p>
// //       ) : (
// //         <table>
// //           <thead>
// //             <tr>
// //               <th>Invoice ID</th>
// //               <th>Quotation ID</th>
// //               <th>Quotation Number</th>
// //               <th>Invoice Number</th>
// //               <th>Total Amount</th>
// //               <th>Paid Amount</th>
// //               <th>Amount Due</th>
// //               <th>Status</th>
// //               <th>Created At</th>
// //               <th>Lead ID</th>
// //               <th>Due Date</th>
// //             </tr>
// //           </thead>
// //           <tbody>
// //             {invoices.map((invoice) => (
// //               <tr key={invoice.id}>
// //                 <td>{invoice.id}</td>
// //                 <td>{invoice.quotation}</td>
// //                 <td>{invoice.quotation_number}</td>
// //                 <td>{invoice.invoice_number}</td>
// //                 <td>{invoice.total_amount}</td>
// //                 <td>{invoice.paid_amount}</td>
// //                 <td>{invoice.amount_due}</td>
// //                 <td>{invoice.status}</td>
// //                 <td>{invoice.created_at}</td>
// //                 <td>{invoice.lead_id ?? 'N/A'}</td>
// //                 <td>{invoice.due_date ?? 'N/A'}</td>
// //               </tr>
// //             ))}
// //           </tbody>
// //         </table>
// //       )}
// //     </div>
// //   );
// // };


// // export default App;


// import type React from 'react';
// import { useState, useEffect } from 'react';

// const Invoice = () => {
//   const [quotationId, setQuotationId] = useState('');
//   const [leadId, setLeadId] = useState('');
//   const [paidAmount, setPaidAmount] = useState('');
//   const [dueDate, setDueDate] = useState('');
//   const [responseMessage, setResponseMessage] = useState('');
//   const [loading, setLoading] = useState(false);

//   interface Invoice {
//     id: number;
//     quotation: number;
//     quotation_number: string;
//     invoice_number: string;
//     total_amount: string;
//     paid_amount: string;
//     amount_due: string;
//     status: string;
//     created_at: string;
//     lead_id?: number;
//     due_date?: string;
//   }

//   const [invoices, setInvoices] = useState<Invoice[]>([]);

//   useEffect(() => {
//     fetchInvoices();
//   }, []);

//   const fetchInvoices = async () => {
//     try {
//       setLoading(true); // Start loading

//       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
//         method: 'GET',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//       });

//       const result = await response.json();
//       console.log("result : ", result);

//       if (response.ok) {
//         setInvoices(result);
//       } else {
//         setResponseMessage(result.error || 'An error occurred.');
//       }
//     } catch (error) {
//       console.error('Error fetching invoices:', error);
//       setResponseMessage('An error occurred while fetching the invoices.');
//     } finally {
//       setLoading(false); // Stop loading
//     }
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
//       setLoading(true); // Start loading

//       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data),
//       });

//       const result = await response.json();
//       console.log("result : ", result);

//       if (response.ok) {
//         setResponseMessage(result.message || 'Invoice created successfully!');
//         fetchInvoices(); // Re-fetch the list of invoices
//       } else {
//         setResponseMessage(result.error || 'An error occurred.');
//       }
//     } catch (error) {
//       console.error('Error creating invoice:', error);
//       setResponseMessage('An error occurred while creating the invoice.');
//     } finally {
//       setLoading(false); // Stop loading
//     }
//   };

//   return (
//     <div>
//       <h2>Create Invoice</h2>
//       <form onSubmit={handleSubmit}>
//         <div>
//           <label>
//             Quotation ID:
//             <input
//               type="number"
//               value={quotationId}
//               onChange={(e) => setQuotationId(e.target.value)}
//               required
//             />
//           </label>
//         </div>
//         <div>
//           <label>
//             Lead ID:
//             <input
//               type="number"
//               value={leadId}
//               onChange={(e) => setLeadId(e.target.value)}
//               required
//             />
//           </label>
//         </div>
//         <div>
//           <label>
//             Paid Amount:
//             <input
//               type="number"
//               value={paidAmount}
//               onChange={(e) => setPaidAmount(e.target.value)}
//               required
//             />
//           </label>
//         </div>
//         <div>
//           <label>
//             Due Date:
//             <input
//               type="datetime-local"
//               value={dueDate}
//               onChange={(e) => setDueDate(e.target.value)}
//               required
//             />
//           </label>
//         </div>
//         <button type="submit" disabled={loading}>
//           {loading ? 'Submitting...' : 'Create Invoice'}
//         </button>
//       </form>

//       {responseMessage && <p>{responseMessage}</p>}

//       <h2>Invoices</h2>
//       {loading ? (
//         <p>Loading...</p>
//       ) : (
//         <table>
//           <thead>
//             <tr>
//               <th>Invoice ID</th>
//               <th>Quotation ID</th>
//               <th>Quotation Number</th>
//               <th>Invoice Number</th>
//               <th>Total Amount</th>
//               <th>Paid Amount</th>
//               <th>Amount Due</th>
//               <th>Status</th>
//               <th>Created At</th>
//               <th>Lead ID</th>
//               <th>Due Date</th>
//             </tr>
//           </thead>
//           <tbody>
//             {invoices.map((invoice) => (
//               <tr key={invoice.id}>
//                 <td>{invoice.id}</td>
//                 <td>{invoice.quotation}</td>
//                 <td>{invoice.quotation_number}</td>
//                 <td>{invoice.invoice_number}</td>
//                 <td>{invoice.total_amount}</td>
//                 <td>{invoice.paid_amount}</td>
//                 <td>{invoice.amount_due}</td>
//                 <td>{invoice.status}</td>
//                 <td>{invoice.created_at}</td>
//                 <td>{invoice.lead_id ?? 'N/A'}</td>
//                 <td>{invoice.due_date ?? 'N/A'}</td>
//               </tr>
//             ))}
//           </tbody>
//         </table>
//       )}
//     </div>
//   );
// };

// export default Invoice;


import type React from 'react';
import { useState, useEffect } from 'react';
import './Invoice.css';

const Invoice = () => {
  const [quotationId, setQuotationId] = useState('');
  const [leadId, setLeadId] = useState('');
  const [paidAmount, setPaidAmount] = useState('');
  const [dueDate, setDueDate] = useState('');
  const [responseMessage, setResponseMessage] = useState('');
  const [loading, setLoading] = useState(false);

  interface Invoice {
    id: number;
    quotation: number;
    quotation_number: string;
    invoice_number: string;
    total_amount: string;
    paid_amount: string;
    amount_due: string;
    status: string;
    created_at: string;
    lead_id?: number;
    due_date?: string;
  }

  const [invoices, setInvoices] = useState<Invoice[]>([]);

  useEffect(() => {
    document.title = 'Invoice';
    fetchInvoices();
  }, []);

  const fetchInvoices = async () => {
    try {
      setLoading(true); // Start loading

      const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      const result = await response.json();
      console.log("result : ", result);

      if (response.ok) {
        setInvoices(result);
      } else {
        setResponseMessage(result.error || 'An error occurred.');
      }
    } catch (error) {
      console.error('Error fetching invoices:', error);
      setResponseMessage('An error occurred while fetching the invoices.');
    } finally {
      setLoading(false); // Stop loading
    }
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const data = {
      quotation_id: quotationId,
      lead_id: leadId,
      paid_amount: paidAmount,
      due_date: dueDate,
    };

    try {
      setLoading(true); // Start loading

      const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      console.log("result : ", result);

      if (response.ok) {
        setResponseMessage(result.message || 'Invoice created successfully!');
        fetchInvoices(); // Re-fetch the list of invoices
      } else {
        setResponseMessage(result.error || 'An error occurred.');
      }
    } catch (error) {
      console.error('Error creating invoice:', error);
      setResponseMessage('An error occurred while creating the invoice.');
    } finally {
      setLoading(false); // Stop loading
    }
  };

  return (
    <div>
      <h2>Create Invoice</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Quotation ID:
            <input
              type="number"
              value={quotationId}
              onChange={(e) => setQuotationId(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Lead ID:
            <input
              type="number"
              value={leadId}
              onChange={(e) => setLeadId(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Paid Amount:
            <input
              type="number"
              value={paidAmount}
              onChange={(e) => setPaidAmount(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Due Date:
            <input
              type="datetime-local"
              value={dueDate}
              onChange={(e) => setDueDate(e.target.value)}
              required
            />
          </label>
        </div>
        <button type="submit" disabled={loading}>
          {loading ? 'Submitting...' : 'Create Invoice'}
        </button>
      </form>

      {responseMessage && <p>{responseMessage}</p>}

      <h2>Invoices</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <table className="invoice-table">
          <thead>
            <tr>
              <th>Invoice ID</th>
              <th>Quotation ID</th>
              <th>Quotation Number</th>
              <th>Invoice Number</th>
              <th>Total Amount</th>
              <th>Paid Amount</th>
              <th>Amount Due</th>
              <th>Status</th>
              <th>Created At</th>
              <th>Lead ID</th>
              <th>Due Date</th>
            </tr>
          </thead>
          <tbody>
            {invoices.map((invoice) => (
              <tr key={invoice.id}>
                <td>{invoice.id}</td>
                <td>{invoice.quotation}</td>
                <td>{invoice.quotation_number}</td>
                <td>{invoice.invoice_number}</td>
                <td>{invoice.total_amount}</td>
                <td>{invoice.paid_amount}</td>
                <td>{invoice.amount_due}</td>
                <td>{invoice.status}</td>
                <td>{invoice.created_at}</td>
                <td>{invoice.lead_id ?? 'N/A'}</td>
                <td>{invoice.due_date ?? 'N/A'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default Invoice;