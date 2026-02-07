import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer
} from 'recharts';
import '../App.css';

const api = axios.create({
    baseURL: "http://localhost:8000",
});

function Dashboard() {
    const [stats, setStats] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        const fetchStats = async () => {
            try {
                const res = await api.get("/dashboard/stats");
                setStats(res.data);
            } catch (err) {
                setError("Failed to fetch dashboard data");
            } finally {
                setLoading(false);
            }
        };
        fetchStats();
    }, []);

    if (loading) return <div className="loader" style={{ textAlign: "center", padding: "40px" }}>Loading Dashboard...</div>;
    if (error) return <div className="error-msg" style={{ maxWidth: "600px", margin: "40px auto" }}>{error}</div>;
    if (!stats) return null;

    return (
        <div className="container">
            <div className="content-grid" style={{ gridTemplateColumns: "1fr" }}>

                {/* Stats Row */}
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '24px', marginBottom: '8px' }}>
                    <div className="card" style={{ textAlign: 'center', padding: '32px' }}>
                        <h2 style={{ fontSize: '14px', color: '#6b7280', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '8px' }}>Total Inventory</h2>
                        <div style={{ fontSize: '56px', fontWeight: '800', color: '#7c3aed', lineHeight: 1 }}>
                            {stats.total_quantity}
                        </div>
                        <p style={{ color: '#9ca3af', marginTop: '8px', fontSize: '14px' }}>Items currently in stock</p>
                    </div>
                </div>

                {/* Graph */}
                <div className="card">
                    <h2 style={{ marginBottom: '24px' }}>Inventory Activity</h2>
                    <div style={{ height: '400px', width: '100%' }}>
                        <ResponsiveContainer width="100%" height="100%">
                            <LineChart
                                data={stats.activity}
                                margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
                            >
                                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e5e7eb" />
                                <XAxis
                                    dataKey="date"
                                    stroke="#6b7280"
                                    tick={{ fontSize: 12 }}
                                    tickLine={false}
                                    axisLine={false}
                                    dy={10}
                                />
                                <YAxis
                                    allowDecimals={false}
                                    stroke="#6b7280"
                                    tick={{ fontSize: 12 }}
                                    tickLine={false}
                                    axisLine={false}
                                    dx={-10}
                                />
                                <Tooltip
                                    contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}
                                />
                                <Legend wrapperStyle={{ paddingTop: '20px' }} />
                                <Line
                                    type="monotone"
                                    dataKey="added"
                                    stroke="#10b981"
                                    name="Items Added"
                                    strokeWidth={3}
                                    dot={{ r: 4, strokeWidth: 2 }}
                                    activeDot={{ r: 6 }}
                                />
                                <Line
                                    type="monotone"
                                    dataKey="deleted"
                                    stroke="#ef4444"
                                    name="Items Deleted"
                                    strokeWidth={3}
                                    dot={{ r: 4, strokeWidth: 2 }}
                                    activeDot={{ r: 6 }}
                                />
                            </LineChart>
                        </ResponsiveContainer>
                    </div>
                    {stats.activity.length === 0 && (
                        <div style={{ textAlign: 'center', color: '#9ca3af', padding: '20px', background: '#f9fafb', borderRadius: '8px', marginTop: '20px' }}>
                            <p style={{ margin: 0 }}>No activity recorded yet.</p>
                            <small>Add or delete items to see the graph populate!</small>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
