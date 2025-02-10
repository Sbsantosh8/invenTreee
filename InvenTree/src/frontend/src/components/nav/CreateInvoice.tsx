import type React from 'react';
import { useState, useEffect } from 'react';
import './Invoice.css';

const CreateInvoice = () => {
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

  interface Quotation {
    id: number;
    name: string;
    lead: number;
  }

  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [quotations, setQuotations] = useState<Quotation[]>([]);

  useEffect(() => {
    document.title = 'Invoice';
    console.log("hii")
    fetchInvoices();  
    fetchQuotations();
  }, []);
console.log("hello...")
  const fetchInvoices = async () => {
    console.log("inside fetchinvoces...")
    try {
      setLoading(true);
      const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/');
      const result = await response.json();
      if (response.ok) {
        setInvoices(result);
      } else {
        setResponseMessage(result.error || 'An error occurred.');
      }
    } catch (error) {
      console.error('Error fetching invoices:', error);
      setResponseMessage('An error occurred while fetching the invoices.');
    } finally {
      setLoading(false);
    }
  };

  const fetchQuotations = async () => {
    console.log("inside fetch quotation...")
    try {
      const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/quotations/');
      const result = await response.json();
      if (response.ok) {
        setQuotations(result);
        
      } else {
        console.error('Failed to fetch quotations:', result.error);
      }
    } catch (error) {
      console.error('Error fetching quotations:', error);
    }
  };

  const handleQuotationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedQuotationId = e.target.value;
    console.log('Selected Quotation ID:', selectedQuotationId);
    setQuotationId(selectedQuotationId);
    

    // Automatically update lead ID when selecting a quotation
    const selectedQuotation = quotations.find((q) => q.id === Number(selectedQuotationId));
    if (selectedQuotation) {
      console.log(selectedQuotation)
      console.log(selectedQuotation.lead)
      setLeadId(String(selectedQuotation.lead))
    } else {
      setLeadId('');
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
        fetchInvoices();
      } else {
        setResponseMessage(result.error || 'An error occurred.');
      }
    } catch (error) {
      console.error('Error creating invoice:', error);
      setResponseMessage('An error occurred while creating the invoice.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Create Invoice</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Quotation Id :
            <select
              value={quotationId}
              onChange={handleQuotationChange}
              required
            >
              <option value="">Select a Quotation</option>
              {quotations.map((quotation) => (
                <option key={quotation.id} value={quotation.id}>
                  {quotation.name || `Quotation ${quotation.id}`}
                </option>
              ))}
            </select>
          </label>
        </div>
        <div>
          <label>
            Lead ID:
            <input
              type="number"
              value={leadId}
              readOnly
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

   
    </div>
  );
};

export default CreateInvoice;
